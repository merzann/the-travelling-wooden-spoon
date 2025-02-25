from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.http import HttpResponse
from .models import WeeklyTip, Subscriber
import csv


@admin.register(WeeklyTip)
class WeeklyTipAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the `WeeklyTip` model.

    **Features:**
    - Displays title, publish date, and creation timestamp in the admin list.
    - Enables filtering by `publish_date`.
    - Allows searching by `title` and `content`.
    - Uses Summernote for the `content` field to enable rich text editing.
    """
    list_display = ('title', 'publish_date', 'created_at')
    list_filter = ('publish_date',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `Subscriber` model.

    **Features:**
    - Displays subscriber's name, email, and subscription date in the admin
      list.
    - Enables searching by name and email.
    - Provides an action to export subscriber data to CSV.
    """
    list_display = ('name', 'email', 'subscribed_at')
    search_fields = ('name', 'email')
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Exports selected subscribers as a CSV file.

        Generates a CSV file with subscriber details and provides it as a
        downloadable response.

        **CSV Fields:**
        - ``Name``
        - ``Email``
        - ``Subscribed At``
        """
        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'
        ] = 'attachment; filename="subscribers.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Email', 'Subscribed At'])

        for subscriber in queryset:
            writer.writerow(
                [subscriber.name, subscriber.email, subscriber.subscribed_at])

        return response

    export_as_csv.short_description = "Export Selected Subscribers as CSV"
