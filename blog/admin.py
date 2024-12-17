from django.contrib import admin
from .models import Category, Recipe, HomepageFeature, BlogPost

# RecipeAdmin with filtering and search
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'popularity_score', 'date')
    list_filter = ('status', 'category')  # Filter by category and status
    search_fields = ('title', 'description')  # Enable search
    prepopulated_fields = {'excerpt': ('description',)}  # Auto-generate excerpt from description


# CategoryAdmin for managing recipe categories
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# HomepageFeatureAdmin for managing featured recipes
@admin.register(HomepageFeature)
class HomepageFeatureAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'excerpt')
    search_fields = ('recipe__title',)


# BlogPostAdmin for managing blog posts
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'snippet')
    ordering = ('-date',)