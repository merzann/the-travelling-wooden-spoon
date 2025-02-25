from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for users to submit comments on recipes.

    **Fields:**
    - ``body``: A text field where users can enter their comment.

    **Meta Class:**
    - ``model``: Specifies that this form is associated with the `Comment`
      model.
    - ``fields``: Defines which fields from the `Comment` model should be
      included in the form.

    **Template:**
    :template:`blog/recipe_detail.html`
    """
    class Meta:
        model = Comment
        fields = ('body',)
