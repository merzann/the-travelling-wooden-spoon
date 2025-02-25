from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model representing a recipe category.

    **Fields**
    - `name` (CharField): Unique name of the category.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Model representing a recipe.

    **Fields**
    - `title` (CharField): Recipe title.
    - `excerpt` (TextField): Short summary of the recipe.
    - `description` (TextField): Full details of the recipe.
    - `image` (CloudinaryField): Recipe image.
    - `category` (ForeignKey): Category of the recipe.
    - `date` (DateTimeField): Date when the recipe was created.
    - `popularity_score` (IntegerField): Score based on user interaction.
    - `status` (IntegerField): Draft or Published status.
    - `total_rating` (DecimalField): Total sum of ratings.
    - `rating_count` (IntegerField): Number of ratings received.

    **Methods:**
    - ``calculate_average_rating``: Computes and returns the average rating.
    """
    STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )

    title = models.CharField(max_length=200)
    excerpt = models.TextField(max_length=450, blank=True, null=True)
    description = models.TextField()
    image = CloudinaryField("image", null=True, blank=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipes",
    )
    date = models.DateTimeField(auto_now_add=True)
    popularity_score = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    total_rating = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0
    )
    rating_count = models.IntegerField(default=0)

    def calculate_average_rating(self):
        if self.rating_count > 0:
            return round(float(self.total_rating) / self.rating_count, 1)
        return 0.0

    def __str__(self):
        return self.title


class HomepageFeature(models.Model):
    """
    Represents a featured recipe on the homepage.

    **Fields:**
    - ``recipe``: A OneToOneField linking to a `Recipe`, ensuring each
      recipe is featured only once.
    - ``excerpt``: A short text summary of the featured recipe (max 300
      characters).

    **Methods:**
    - ``__str__``: Returns a formatted string representation of the featured
      recipe.
    """
    recipe = models.OneToOneField(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="featured",
    )
    excerpt = models.TextField(max_length=300)

    def __str__(self):
        return f"Featured: {self.recipe.title}"


class BlogPost(models.Model):
    """
    Represents a blog post related to a specific recipe.

    **Fields:**
    - ``recipe``: A ForeignKey linking to `Recipe`, allowing multiple
      blog posts for a single recipe.
    - ``title``: The title of the blog post.
    - ``image``: An optional image for the blog post (stored via Cloudinary).
    - ``snippet``: A short preview text for the blog post (max 300
      characters).
    - ``content``: The main body content of the blog post.
    - ``date``: The date and time when the blog post was created
      (auto-generated).

    **Methods:**
    - ``__str__``: Returns the blog post title.
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=200)
    image = CloudinaryField("image", null=True, blank=True)
    snippet = models.TextField(max_length=300)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Recipe`.

    **Fields:**
    - ``recipe``: A ForeignKey linking to a `Recipe`, allowing multiple
      comments per recipe.
    - ``user``: A ForeignKey linking to `User`, representing the comment
      author.
    - ``body``: The text content of the comment.
    - ``timestamp``: The date and time when the comment was created
      (auto-generated).
    - ``approved``: A boolean flag to indicate whether the comment is
      approved by an admin.

    **Methods:**
    - ``__str__``: Returns a formatted string representation of the
      comment and its author.
    """
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user} on {self.recipe.title}"
