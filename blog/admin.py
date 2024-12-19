from django.contrib import admin
from .models import Category, Recipe, HomepageFeature, BlogPost, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'category', 'status', 'popularity_score', 'date')
    search_fields = ['title', 'description']
    list_filter = ('status', 'category')
    prepopulated_fields = {'excerpt': ('description',)}
    summernote_fields = ('content',)

# RecipeAdmin with filtering and search
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'popularity_score', 'date')
    list_filter = ('status', 'category') 
    search_fields = ('title', 'description')
    prepopulated_fields = {'excerpt': ('description',)}


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


# CommentAdmin for managing comments
@admin.register(Comment)
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