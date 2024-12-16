from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# Category model to organize recipes into groups
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Recipe model to store details of each recipe
class Recipe(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True, null=True)  # For homepage
    image = CloudinaryField('image', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='recipes')
    date = models.DateTimeField(auto_now_add=True)
    popularity_score = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)  # Draft by default

    def __str__(self):
        return self.title
