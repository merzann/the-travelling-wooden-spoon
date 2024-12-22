from django.test import TestCase
from .models import About
from django.db import models
from cloudinary.models import CloudinaryField

class AboutModelTest(TestCase):
    def setUp(self):
        # Set up test data for the About model
        self.about = About.objects.create(
            bio="This is a test bio.",
            profile_picture="sample_image.jpg"  # Mocked Cloudinary image path
        )

    def test_about_creation(self):
        # Test that the About instance is created successfully
        self.assertIsInstance(self.about, About)

    def test_about_bio_content(self):
        # Test that the bio field contains the correct content
        self.assertEqual(self.about.bio, "This is a test bio.")

    def test_about_profile_picture(self):
        # Test that the profile picture field is set correctly
        self.assertEqual(self.about.profile_picture, "sample_image.jpg")

    def test_about_str_method(self):
        # Test the __str__ method of the About model
        self.assertEqual(str(self.about), "About Page Content")
