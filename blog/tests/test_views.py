from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Category, Recipe, HomepageFeature, BlogPost, Comment
from weekly_tip.models import Subscriber

class HomepageViewTests(TestCase):
    def setUp(self):
        # Set up sample data
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            excerpt="A short description of the cake.",
            description="A detailed description of the cake.",
            category=self.category,
            status=1
        )
        self.blog_post = BlogPost.objects.create(
            title="Test Blog Post",
            recipe=self.recipe,
            snippet="This is a test snippet.",
            content="This is a test blog post content."
        )
        self.featured = HomepageFeature.objects.create(recipe=self.recipe)

    def test_homepage_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_homepage_context(self):
        response = self.client.get(reverse('home'))
        self.assertIn('categories', response.context)
        self.assertIn('featured_recipes', response.context)
        self.assertIn('latest_recipes', response.context)
        self.assertIn('popular_recipes', response.context)
        self.assertIn('latest_blog_posts', response.context)

    def test_newsletter_signup_success(self):
        response = self.client.post(reverse('home'), data={
            'name': 'John Doe',
            'email': 'john@example.com',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Subscriber.objects.filter(email='john@example.com').exists())

class BlogDetailViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Recipe for Testing",
            description="Detailed recipe description.",
            status=1
        )
        self.blog_post = BlogPost.objects.create(
            title="Test Blog Post",
            recipe=self.recipe,
            snippet="This is a snippet.",
            content="This is the full content of the blog post."
        )

    def test_blog_detail_template_used(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/recipe_detail.html')

    def test_blog_detail_context(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog_post.id]))
        self.assertEqual(response.context['blog_post'], self.blog_post)
        self.assertEqual(response.context['recipe'], self.recipe)

class RecipesViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Sample Recipe",
            description="Recipe description",
            status=1
        )

    def test_recipes_view(self):
        response = self.client.get(reverse('recipes_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category.html')
        self.assertIn('recipes', response.context)

class CategoryViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Appetizers")
        self.recipe = Recipe.objects.create(
            title="Sample Appetizer",
            description="Appetizer description",
            category=self.category,
            status=1
        )

    def test_category_view(self):
        response = self.client.get(reverse('category_view', args=[self.category.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category.html')
        self.assertEqual(response.context['category'], self.category)

class RecipeDetailViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="Detailed Recipe",
            description="This is a detailed recipe.",
            status=1
        )

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/recipe_detail.html')
        self.assertEqual(response.context['recipe'], self.recipe)

class DeleteCommentViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Recipe description",
            status=1
        )
        self.comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            body="Sample comment"
        )

    def test_delete_comment(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_comment', args=[self.comment.id]))
        self.assertRedirects(response, reverse('recipe_detail', args=[self.recipe.id]))
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())
