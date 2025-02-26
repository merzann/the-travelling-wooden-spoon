from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    """
    Replaces default Allauth sign-up form to make the email field mandatory
    Adds custom label

    **Fields:**
    - ``email``: A required email field for user registration.

    **Methods:**
    - ``__init__``: Ensures the email field is required and updates its label.
    - ``save``: Saves the user instance and ensures the email is stored
      correctly.

    **Template:**
    :template:`account/signup.html`
    """

    email = forms.EmailField(
        required=True,
        label="Email Address",  # Explicitly set the label here
        widget=forms.EmailInput(attrs={"placeholder": "Your Email Address"}),
    )

    def __init__(self, *args, **kwargs):
        """
        Ensure email field is required and update label on initialization.
        """
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        self.fields["email"].label = "Email Address"

    def save(self, request):
        """
        Saves the user instance and assigns email value before saving.

        **Returns:**
        - ``user``: The created or updated user instance.
        """
        user = super().save(request)
        user.email = self.cleaned_data["email"]
        user.save()
        return user
