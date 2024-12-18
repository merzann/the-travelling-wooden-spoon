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
tracks thumbs-up/thumbs-down ratings
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
    thumbs_up = models.PositiveIntegerField(default=0)
    thumbs_down = models.PositiveIntegerField(default=0)

    def calculate_average_rating(self):
        """function to track rating"""
        ratings = self.ratings.all()
        if ratings.exists():
            total_score = sum(rating.score for rating in ratings)
            return total_score / ratings.count()
        return 0

    def total_votes(self):
        return self.ratings.count()

    def __str__(self):
        return self.title


# Star rating 1–5
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ratings', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.recipe.title} - {self.score}'


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

