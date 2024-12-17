from django.shortcuts import render
from .models import Recipe, HomepageFeature, BlogPost

# Create your views here.

# Homepage View
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

