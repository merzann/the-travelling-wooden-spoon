from django.contrib import admin
from django.db import models
from .models import Category, Recipe, HomepageFeature, BlogPost, Comment
from django_summernote.widgets import SummernoteWidget
from django_summernote.admin import SummernoteModelAdmin


# Summernote dynamic regristration
class DynamicSummernoteAdmin(SummernoteModelAdmin):
    """Custom admin to apply Summernote to all TextFields dynamically."""
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        for field in self.model._meta.get_fields():
            if isinstance(field, models.TextField):
                form.base_fields[field.name].widget = SummernoteWidget()
        
        return form


# Register the models with the custom admin class
admin.site.register(Category, DynamicSummernoteAdmin)
admin.site.register(Recipe, DynamicSummernoteAdmin)
admin.site.register(HomepageFeature, DynamicSummernoteAdmin)
admin.site.register(BlogPost, DynamicSummernoteAdmin)
admin.site.register(Comment, DynamicSummernoteAdmin)


# RecipeAdmin with filtering and search
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'popularity_score', 'date')
    list_filter = ('status', 'category') 
    search_fields = ('title', 'description')
    prepopulated_fields = {'excerpt': ('description',)}


# CategoryAdmin for managing recipe categories
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# HomepageFeatureAdmin for managing featured recipes
class HomepageFeatureAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'excerpt')
    search_fields = ('recipe__title',)


# BlogPostAdmin for managing blog posts
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'snippet')
    ordering = ('-date',)


# CommentAdmin for managing comments
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user', 'approved', 'timestamp')
    list_filter = ('approved', 'timestamp')
    search_fields = ('user', 'text')
    actions = ['approve_comments', 'disapprove_comments']

    # Custom action to approve comments
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

    # Custom action to disapprove comments
    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
    disapprove_comments.short_description = "Disapprove selected comments"