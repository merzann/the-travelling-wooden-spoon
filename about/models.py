from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    bio = models.TextField()
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return "About Page Content"
