from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


@admin.register(About)
class AboutPageAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing About Page content.

    **Features:**
    - Uses Summernote for rich text editing of the `bio` field.
    """
    summernote_fields = ('bio',)
