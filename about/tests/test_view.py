class AboutPageViewTest(TestCase):
    def setUp(self):
        # Set up test data and client
        self.client = Client()
        self.about = About.objects.create(
            bio="This is a test bio.",
            profile_picture="sample_image.jpg"  # Mocked Cloudinary image path
        )

    def test_about_page_view_status_code(self):
        # Test that the about page returns a 200 status code
        response = self.client.get(reverse('about_page'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_context(self):
        # Test that the context contains the correct data
        response = self.client.get(reverse('about_page'))
        self.assertIn('bio', response.context)
        self.assertIn('profile_picture', response.context)
        self.assertEqual(response.context['bio'], "This is a test bio.")
        self.assertEqual(response.context['profile_picture'], "sample_image.jpg")

    def test_about_page_template(self):
        # Test that the correct template is used
        response = self.client.get(reverse('about_page'))
        self.assertTemplateUsed(response, 'about/about.html')
