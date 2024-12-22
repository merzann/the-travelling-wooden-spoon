from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Category, Recipe, HomepageFeature, BlogPost, Comment

class CategoryModelTest(TestCase):
    def test_string_representation(self):
        category = Category.objects.create(name="Desserts")
        self.assertEqual(str(category), "Desserts")


class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
        title="Chocolate Cake",
        excerpt="A delicious chocolate cake recipe.",
        description="This is a full description of the chocolate cake recipe.",
        category=self.category,
        total_rating=45.0,  # Adjusted for consistency
        rating_count=10,
        status=1
    )


    def test_string_representation(self):
        self.assertEqual(str(self.recipe), "Chocolate Cake")

    def test_calculate_average_rating(self):
        self.assertEqual(self.recipe.calculate_average_rating(), 4.5)

    def test_default_popularity_score(self):
        new_recipe = Recipe.objects.create(
            title="Vanilla Cake",
            description="Description for vanilla cake.",
            category=self.category
        )
        self.assertEqual(new_recipe.popularity_score, 0)


class HomepageFeatureModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Description for chocolate cake.",
            category=self.category
        )
        self.feature = HomepageFeature.objects.create(
            recipe=self.recipe,
            excerpt="Featured Chocolate Cake!"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.feature), "Featured: Chocolate Cake")


class BlogPostModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Description for chocolate cake.",
            category=self.category
        )
        self.blog_post = BlogPost.objects.create(
            recipe=self.recipe,
            title="Blog Post Title",
            snippet="Snippet of the blog post.",
            content="Full content of the blog post."
        )

    def test_string_representation(self):
        self.assertEqual(str(self.blog_post), "Blog Post Title")


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Description for chocolate cake.",
            category=self.category
        )
        self.comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            body="This is a comment."
        )

    def test_string_representation(self):
        self.assertEqual(str(self.comment), "Comment by testuser on Chocolate Cake")

    def test_comment_default_approval(self):
        self.assertFalse(self.comment.approved)
