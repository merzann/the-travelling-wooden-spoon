from django.shortcuts import render
from .models import About

def about_page(request):
    about_content = About.objects.first()  # Assuming a single record for simplicity
    context = {
        'bio': about_content.bio if about_content else "Bio not yet set.",
        'profile_picture': about_content.profile_picture if about_content else None
    }
    return render(request, 'about/about.html', context)
