from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Recipe, HomepageFeature, BlogPost, Comment
from .forms import CommentForm
from weekly_tip.models import Subscriber

from django.test import TestCase
from django.urls import reverse

# displays content on homepage

def homepage(request):
    # Query data for homepage sections
    categories = Category.objects.all()
    featured_recipes = HomepageFeature.objects.select_related(
        'recipe').order_by('-recipe__total_rating')[:3]
    latest_recipes = Recipe.objects.filter(status=1).order_by('-date')[:3]
    popular_recipes = Recipe.objects.filter(
        status=1).order_by('-popularity_score')[:3]
    latest_blog_posts = BlogPost.objects.filter(
        recipe__status=1).order_by('-date')[:3]

    # Newsletter sign-up handling
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Handle newsletter sign-up
        if name and email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(name=name, email=email)
                messages.success(request, 'You have successfully signed up for the newsletter.')
            else:
                messages.warning(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Both name and email are required.')

    # Pass data to the template
    context = {
        'categories': categories,
        'featured_recipes': featured_recipes,
        'latest_recipes': latest_recipes,
        'popular_recipes': popular_recipes,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'blog/index.html', context)



# fetches BlogPost and displays content in Latest-Blog-Post-Section when a
# new recipe is posted
def blog_detail(request, blog_id):
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    recipe_description = blog_post.recipe.description if blog_post.recipe else "Description not available."
    return render(request, 'blog/recipe_detail.html', {
        'recipe': blog_post.recipe,
        'description': recipe_description,
        'title': blog_post.title,
        'blog_post': blog_post,
    })


# display all recipes on category.html and categories in dropdown navbar list
def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/category.html', {'recipes': recipes})


def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    recipes = Recipe.objects.filter(category=category)

    for recipe in recipes:
        recipe.average_rating = recipe.calculate_average_rating()

    context = {
        "category": category,
        "recipes": recipes,
    }

    return render(request, 'blog/category.html',
                  {'category': category, 'recipes': recipes})


# display recipe details and rating on recipe_detail.html
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.filter(approved=True)
    form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseForbidden(
                "You must be logged in to perform this action.")

        if "rating" in request.POST:
            # Handle rating submission
            star_rating = int(request.POST.get("rating", 0))
            if 1 <= star_rating <= 5:
                recipe.total_rating += star_rating
                recipe.rating_count += 1
                recipe.save()
        elif "body" in request.POST:
            # Handle comment submission
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.recipe = recipe
                comment.user = request.user if request.user.is_authenticated else "Anonymous"
                comment.save()
                messages.success(
                    request, "Your comment has been submitted and is pending approval.")
                form = CommentForm()
            else:
                messages.error(
                    request, "There was an error submitting your comment.")

    context = {
        "recipe": recipe,
        "average_rating": recipe.calculate_average_rating(),
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/recipe_detail.html", context)


# allow user to delete their own comments
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Ensure only the owner of a comment can delete
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
    else:
        messages.error(
            request,
            "You are not authorized to delete this comment.")
    return redirect('recipe_detail', recipe_id=comment.recipe.id)
