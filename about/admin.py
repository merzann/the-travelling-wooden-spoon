from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutPageAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio',)
