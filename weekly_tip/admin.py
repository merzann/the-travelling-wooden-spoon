from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import WeeklyTip, Subscriber

@admin.register(WeeklyTip)
class WeeklyTipAdmin(SummernoteModelAdmin):
    list_display = ('title', 'publish_date', 'created_at')
    list_filter = ('publish_date',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribed_at')
    search_fields = ('name', 'email')
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="subscribers.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Email', 'Subscribed At'])

        for subscriber in queryset:
            writer.writerow([subscriber.name, subscriber.email, subscriber.subscribed_at])

        return response

    export_as_csv.short_description = "Export Selected Subscribers as CSV"

