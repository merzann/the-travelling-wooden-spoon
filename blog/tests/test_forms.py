from django.test import TestCase
from blog.forms import CommentForm


class CommentFormTest(TestCase):
    def test_valid_comment_form(self):
        # Test with valid data
        form_data = {"body": "This is a test comment."}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_comment_form(self):
        # Test with empty data
        form_data = {"body": ""}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_comment_form_without_body_field(self):
        # Test with missing body field
        form_data = {}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())