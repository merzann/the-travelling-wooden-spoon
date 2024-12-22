from django.contrib import admin
from django.db import models
from .models import Category, Recipe, HomepageFeature, BlogPost, Comment
from django_summernote.widgets import SummernoteWidget
from django_summernote.admin import SummernoteModelAdmin


# Dynamic Summernote for generic models
class DynamicSummernoteAdmin(SummernoteModelAdmin):
    """Custom admin to apply Summernote to all TextFields dynamically."""

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for field in self.model._meta.get_fields():
            if isinstance(field, models.TextField):
                form.base_fields[field.name].widget = SummernoteWidget()
        return form


# Explicit Admin for Comment Model
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """Custom admin with filters and Summernote for the Comment model."""
    list_display = ('recipe', 'user', 'approved', 'timestamp')
    list_filter = ('approved', 'timestamp')  # Restore filters
    search_fields = ('user__username', 'body')
    actions = ['approve_comments', 'disapprove_comments']

    # Custom actions
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
    disapprove_comments.short_description = "Disapprove selected comments"


# Explicit Admin for Recipe Model
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Custom admin for the Recipe model."""
    list_display = ('title', 'category', 'status', 'popularity_score', 'date')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')
    prepopulated_fields = {'excerpt': ('description',)}
    summernote_fields = ('description',)


# Dynamic Registration for Other Models
models_to_register = [Category, HomepageFeature]
for model in models_to_register:
    if not admin.site.is_registered(model):
        admin.site.register(model, DynamicSummernoteAdmin)
