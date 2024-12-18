from django.shortcuts import render
from .models import Category, Recipe, HomepageFeature, BlogPost

# Create your views here.

# displays content on homepage
def homepage(request):
    # Query data for homepage sections
    featured_recipes = HomepageFeature.objects.select_related('recipe')[:3]  # Limit to 3 featured recipes
    latest_recipes = Recipe.objects.filter(status=1).order_by('-date')[:3]  # Limit to 3 latest recipes
    popular_recipes = Recipe.objects.filter(status=1).order_by('-popularity_score')[:3]  # Limit to 3 popular recipes
    latest_blog_posts = BlogPost.objects.all().order_by('-date')[:3]  # Limit to 3 latest blog posts

    # Pass data to the template
    context = {
        'featured_recipes': featured_recipes,
        'latest_recipes': latest_recipes,
        'popular_recipes': popular_recipes,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'blog/index.html', context)


# displays all posted recipes sorted in categries on category.html
from django.shortcuts import render
from .models import Recipe

def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/category.html', {'recipes': recipes})


def category_view(request, category_name):
    # Get the category object by name
    category = get_object_or_404(Category, name=category_name)
    # Fetch all recipes under this category
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'blog/category.html', {'category': category, 'recipes': recipes})


# Recipe_detail model to display/view recipe details
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    average_rating = recipe.calculate_average_rating()
    total_votes = recipe.total_votes()
    
    context = {
        'recipe': recipe,
        'thumbs_up': recipe.thumbs_up,
        'thumbs_down': recipe.thumbs_down,
        'average_rating': average_rating,
        'total_votes': total_votes,
    }
    return render(request, 'recipe_detail.html', context)
