from django.contrib import admin
from .models import Category, Recipe

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