from django.shortcuts import render, get_object_or_404
from .models import Category, Recipe, HomepageFeature, BlogPost

# Create your views here.

# displays content on homepage
def homepage(request):
    # Query data for homepage sections
    categories = Category.objects.all()
    featured_recipes = HomepageFeature.objects.select_related('recipe')[:3]
    latest_recipes = Recipe.objects.filter(status=1).order_by('-date')[:3]
    popular_recipes = Recipe.objects.filter(status=1).order_by('-popularity_score')[:3]
    latest_blog_posts = BlogPost.objects.all().order_by('-date')[:3]

    # Pass data to the template
    context = {
        'categories': categories,
        'featured_recipes': featured_recipes,
        'latest_recipes': latest_recipes,
        'popular_recipes': popular_recipes,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'blog/index.html', context)

# display all recipes on category.html and categories in dropdown navbar list
def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/category.html', {'recipes': recipes})


def category_view(request, category_name):
    # Get the category object by name
    category = get_object_or_404(Category, name=category_name)
    # Fetch all recipes under this category
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'blog/category.html', {'category': category, 'recipes': recipes})


# display recipe details on recipe_detail.html
from django.db.models import Avg

def recipe_detail(request, recipe_id):
    # Fetch the recipe by ID
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'blog/recipe_detail.html', {
        'recipe': recipe,
    })

