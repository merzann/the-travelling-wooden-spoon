from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Recipe, HomepageFeature, BlogPost, Comment
from .forms import CommentForm
from weekly_tip.models import Subscriber
from django.http import HttpResponseForbidden


def homepage(request):
    """
    Display the homepage with featured recipes, latest blog posts, and popular
    recipes.

    **Context**

    ``categories``: Queryset of all available recipe categories.
    ``featured_recipes``: Queryset of the top 3 highest-rated featured recipes.
    ``latest_recipes``: Queryset of the latest 3 published recipes.
    ``popular_recipes``: Queryset of the 3 most popular recipes based on
    `popularity_score`.
    ``latest_blog_posts``: Queryset of the latest 3 blog posts linked to
    recipes.

    Handles newsletter sign-up:
    - Users can subscribe by submitting their name and email.
    - Checks for duplicate subscriptions before adding new subscribers.
    - Displays appropriate success or error messages.

    **Template:**
    :template:`blog/index.html`
    """
    categories = Category.objects.all()
    featured_recipes = HomepageFeature.objects.select_related(
        'recipe'
    ).order_by('-recipe__total_rating')[:3]
    latest_recipes = Recipe.objects.filter(status=1).order_by('-date')[:3]
    popular_recipes = Recipe.objects.filter(status=1).all().order_by(
        '-popularity_score', '-rating_count'
    )[:3]
    latest_blog_posts = BlogPost.objects.filter(
        recipe__status=1
    ).order_by('-date')[:3]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(name=name, email=email)
                messages.success(
                    request, 'You have successfully signed up for the '
                    'newsletter.'
                )
            else:
                messages.warning(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Both name and email are required.')

    context = {
        'categories': categories,
        'featured_recipes': featured_recipes,
        'latest_recipes': latest_recipes,
        'popular_recipes': popular_recipes,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'blog/index.html', context)


def blog_detail(request, blog_id):
    """
    Display a blog post with its associated recipe description.

    **Context:**
    - ``blog_post``: An instance of `BlogPost`.
    - ``recipe``: The associated `Recipe` instance (if available).
    - ``description``: The description of the associated recipe.

    **Template:**
    :template:`blog/recipe_detail.html`
    """
    blog_post = get_object_or_404(BlogPost, id=blog_id)
    recipe_description = blog_post.recipe.description if blog_post.recipe \
        else "Description not available."
    return render(
        request,
        'blog/recipe_detail.html',
        {
            'recipe': blog_post.recipe,
            'description': recipe_description,
            'title': blog_post.title,
            'blog_post': blog_post,
        },
    )


def recipes_view(request):
    """
    Display all available recipes on the category page.

    **Context**

    ``recipes``: Queryset of all `Recipe` instances.

    **Template:**
    :template:`blog/category.html`
    """
    recipes = Recipe.objects.all()
    return render(request, 'blog/category.html', {'recipes': recipes})


def category_view(request, category_name):
    """
    Display all recipes within a specific category.
    """
    category = get_object_or_404(Category, name=category_name)
    recipes = Recipe.objects.filter(category=category)

    for recipe in recipes:
        recipe.average_rating = recipe.calculate_average_rating()

    return render(
        request,
        'blog/category.html',
        {'category': category, 'recipes': recipes},
    )


def recipe_detail(request, recipe_id):
    """
    Display details of a specific recipe, including its comments and rating.
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.filter(approved=True)
    form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseForbidden(
                "You must be logged in to perform this action."
            )

        if "rating" in request.POST:
            star_rating = int(request.POST.get("rating", 0))
            if 1 <= star_rating <= 5:
                recipe.total_rating += star_rating
                recipe.rating_count += 1
                recipe.popularity_score = recipe.calculate_average_rating()
                recipe.save()
        elif "body" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.recipe = recipe
                comment.user = request.user if request.user.is_authenticated \
                    else "Anonymous"
                comment.save()
                messages.success(
                    request,
                    "Your comment has been submitted and is pending approval."
                )
                form = CommentForm()
            else:
                messages.error(
                    request, "There was an error submitting your comment."
                )

    context = {
        "recipe": recipe,
        "description": recipe.description,
        "average_rating": recipe.calculate_average_rating(),
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/recipe_detail.html", context)


@login_required
def delete_comment(request, comment_id):
    """
    Allow a user to delete their own comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
    else:
        messages.error(
            request,
            "You are not authorized to delete this comment."
        )
    return redirect('recipe_detail', recipe_id=comment.recipe.id)
