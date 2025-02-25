from django.shortcuts import render
from .models import About


def about_page(request):
    """
    Display the About page with biography and profile picture.

    **Context:**
    - ``bio``: The biography text from the About model.
    - ``profile_picture``: The profile picture from the About model.

    If no About content exists, default values are displayed.

    **Template:**
    :template:`about/about.html`
    """
    about_content = About.objects.first()
    context = {
        'bio': about_content.bio if about_content else "Bio not yet set.",
        'profile_picture': (
            about_content.profile_picture if about_content else None
        ),
    }
    return render(request, 'about/about.html', context)
