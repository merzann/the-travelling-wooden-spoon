from django.test import TestCase
from blog.models import Recipe, BlogPost, Category
from django.db.models.signals import post_save
from unittest.mock import Mock


class SignalsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_blog_post_creation_signal_triggered(self):
        mock_handler = Mock()
        # Connect the mock handler to the post_save signal
        post_save.connect(mock_handler, sender=Recipe)

        recipe = Recipe.objects.create(
            title="Test Recipe",
            excerpt="This is a test excerpt.",
            description="This is a test description.",
            category=self.category,
            status=1,  # Published status
        )

        # Assert that the mock handler was called
        self.assertTrue(mock_handler.called)
        mock_handler.assert_called_once()

        # Disconnect the mock handler
        post_save.disconnect(mock_handler, sender=Recipe)

    def test_blog_post_created_on_recipe_publish(self):
        recipe = Recipe.objects.create(
            title="Test Recipe",
            excerpt="This is a test excerpt.",
            description="This is a test description.",
            category=self.category,
            status=1,  # Published status
        )
        blog_post = BlogPost.objects.get(recipe=recipe)
        self.assertEqual(blog_post.title, f"Recipe Spotlight: {recipe.title}")
        self.assertEqual(blog_post.content, recipe.description)

