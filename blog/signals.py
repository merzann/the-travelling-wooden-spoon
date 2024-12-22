# blog/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Recipe, BlogPost

# Check if a recipe is published


@receiver(post_save, sender=Recipe)
def create_blog_post(sender, instance, created, **kwargs):
    if created and instance.status == 1:
        BlogPost.objects.create(
            recipe=instance,
            title=f"Recipe Spotlight: {instance.title}",
            image=instance.image,
            snippet=instance.excerpt or instance.description[:300],
            content=instance.description,
        )
