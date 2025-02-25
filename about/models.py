from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Represents the About Page content.

    **Fields:**
    - ``bio``: A text field storing the About page content.
    - ``profile_picture``: An optional Cloudinary image for the profile.

    **Methods:**
    - ``__str__``: Returns a string representation of the About Page.
    """
    bio = models.TextField()
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return "About Page Content"
