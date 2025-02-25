from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Recipe, BlogPost


@receiver(post_save, sender=Recipe)
def create_blog_post(sender, instance, created, **kwargs):
    """
    Automatically creates a `BlogPost` when a new `Recipe` is published.

    **Triggers:** 
    - Fires when a `Recipe` instance is created with `status=1` (Published).

    **BlogPost Fields:**
    - `recipe`: Links to the published recipe.
    - `title`: Prefixed with "Recipe Spotlight".
    - `image`: Uses the recipe image.
    - `snippet`: Uses the excerpt or first 300 characters of the description.
    - `content`: Full recipe description.

    **Model:**
    :model:`blog.BlogPost`
    """
    if created and instance.status == 1:
        BlogPost.objects.create(
            recipe=instance,
            title=f"Recipe Spotlight: {instance.title}",
            image=instance.image,
            snippet=instance.excerpt or instance.description[:300],
            content=instance.description,
        )
