from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib import messages
from .models import WeeklyTip, Subscriber


def weekly_tip(request):
    """
    Retrieves and displays the latest published weekly tip.

    **Context:**
    - ``tip``: The latest `WeeklyTip` that has a `publish_date` up to today.

    Handles newsletter sign-up:
    - Users can subscribe by submitting their name and email.
    - Checks for duplicate subscriptions before adding new subscribers.
    - Displays appropriate success or error messages.

    **Template:**
    :template:`weekly_tip/weekly_tip.html`
    """
    tip = WeeklyTip.objects.filter(publish_date__lte=now()).first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(name=name, email=email)
                messages.success(
                    request, 'You have successfully signed up for the '
                    'newsletter.')
            else:
                messages.warning(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Both name and email are required.')

        return redirect('weekly_tip')

    return render(request, 'weekly_tip/weekly_tip.html', {'tip': tip})
