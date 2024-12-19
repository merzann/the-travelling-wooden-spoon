from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id',)
    fields = ('bio', 'profile_picture')
