from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# Category model to organize recipes into groups
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Recipe model
"""
stores all information about recipes
calculate and return rating
"""
class Recipe(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True, null=True)
    image = CloudinaryField('image', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='recipes')
    date = models.DateTimeField(auto_now_add=True)
    popularity_score = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    rating_count = models.IntegerField(default=0)

    def calculate_average_rating(self):
        if self.rating_count > 0:
            return round(self.total_rating / self.rating_count, 2)
        return 0.0

    def __str__(self):
        return self.title


# HomepageFeature model to manage featured recipes displayed on homepage
class HomepageFeature(models.Model):
    recipe = models.OneToOneField('Recipe', on_delete=models.CASCADE, related_name='featured')
    excerpt = models.TextField(max_length=100)

    def __str__(self):
        return f"Featured: {self.recipe.title}"


# Blogpost model to store blogs for latest-blog-post-section
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    snippet = models.TextField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

