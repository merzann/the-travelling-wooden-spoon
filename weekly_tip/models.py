from django.db import models
from cloudinary.models import CloudinaryField


class WeeklyTip(models.Model):
    """
    Represents a weekly tip entry containing a title, content, optional image,
    and publishing details.

    **Fields:**
    - ``title``: Title of the tip (max 200 characters).
    - ``content``: Detailed tip content.
    - ``image``: Optional image associated with the tip.
    - ``publish_date``: Date when the tip is scheduled for publication.
    - ``created_at``: Timestamp of when the tip was created.

    **Meta:**
    - Orders weekly tips by the latest `publish_date` first.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    """
    Represents a newsletter subscriber.

    **Fields:**
    - ``name``: Subscriber's name (max 100 characters).
    - ``email``: Unique email address for the subscriber.
    - ``subscribed_at``: Timestamp of when the subscription was created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
