from django.contrib import admin
from django.db import models
from django_summernote.widgets import SummernoteWidget
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Recipe, HomepageFeature, Comment


# Dynamic Summernote for generic models
class DynamicSummernoteAdmin(SummernoteModelAdmin):
    """
    Custom admin class that applies the Summernote editor to all
    TextFields dynamically.

    **Functionality:**
    - Overrides the default admin form to apply the Summernote
      widget to all TextFields.

    **Methods:**
    - `get_form`: Modifies form fields dynamically to use Summernote.

    **Applied To:**
    - Any model registered using this admin class.
    """
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        for field in self.model._meta.get_fields():
            if isinstance(field, models.TextField):
                form.base_fields[field.name].widget = SummernoteWidget()
        return form


# Explicit Admin for Comment Model
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the `Comment` model.

    **Features:**
    - Displays relevant comment details (`recipe`, `user`, `approved`,
      `timestamp`).
    - Provides filters for `approved` status and timestamp.
    - Enables search functionality for `user__username` and comment `body`.
    - Allows bulk approval or disapproval of comments.

    **Actions:**
    - `approve_comments`: Marks selected comments as approved.
    - `disapprove_comments`: Marks selected comments as disapproved.
    """
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
    """
    Admin configuration for the `Recipe` model.

    **Features:**
    - Displays key details (`title`, `category`, `status`,
      `popularity_score`, `date`).
    - Provides filters for `status` and `category`.
    - Enables search functionality for `title` and `description`.
    - Uses `excerpt` field prepopulated from `description`.
    - Applies Summernote to the `description` field for rich-text editing.

    **Fields:**
    - `title`: Recipe title.
    - `category`: Associated category.
    - `status`: Indicates if the recipe is published or draft.
    - `popularity_score`: Score based on user interactions.
    - `date`: Creation date of the recipe.
    """
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
