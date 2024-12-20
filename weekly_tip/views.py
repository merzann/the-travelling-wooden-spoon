from django.shortcuts import render
from django.utils.timezone import now
from .models import WeeklyTip, Subscriber
from django.contrib import messages

def weekly_tip(request):
    """Get the latest published tip"""
    tip = WeeklyTip.objects.filter(publish_date__lte=now()).first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Handle newsletter sign-up
        if name and email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(name=name, email=email)
                messages.success(request, 'You have successfully signed up for the newsletter.')
            else:
                messages.warning(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Both name and email are required.')

    return render(request, 'weekly_tip/weekly_tip.html', {'tip': tip})
