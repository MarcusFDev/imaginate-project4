import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserProfile, NewsletterSignup


class RegistrationForm(forms.ModelForm):
    """
    A form for user registration that includes username, email, password,
    and password confirmation fields. Provides validation for unique usernames,
    email addresses, password strength, and matching passwords.

    Fields:
        username: TextInput for the username.
        email: EmailInput for the email address.
        password: PasswordInput for the password.
        password_confirm: PasswordInput for confirming the password.
    """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        }), label='Confirm Password'
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email address'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and appends CSS classes for valid/invalid states
        based on form validation errors.
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'
            else:
                self.fields[field].widget.attrs['class'] += ' is-valid'

    def clean_username(self):
        """
        Validates the username by checking:
        - Uniqueness in the database.
        - Maximum length (12 characters).
        - Presence of only alphanumeric characters (no special characters).
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "This username has already been taken.")

        if len(username) > 12:
            raise forms.ValidationError(
                "Username must be no more than 12 characters long.")

        # Check for special characters
        if not re.match(r'^[a-zA-Z0-9]*$', username):
            raise forms.ValidationError(
                "Username must contain only letters and numbers "
                "(no special characters).")

        return username

    def clean_email(self):
        """
        Validates the email to ensure it is unique in the database.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email

    def clean(self):
        """
        Cleans and validates the form by:
        - Checking if the two password fields match.
        - Validating password length, digit inclusion, and special characters.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # Check if passwords match
        if password and password_confirm and password != password_confirm:
            # Attach error to the password_confirm field
            self.add_error('password_confirm', forms.ValidationError(
                "Passwords do not match."))

        # Validate password length
        if password:
            # Ensures password is between 8 and 20 characters long.
            if len(password) < 8 or len(password) > 20:
                self.add_error('password', forms.ValidationError(
                    "Password must be between 8 and 20 characters."))

            # Validate for at least one digit
            if not re.search(r'\d', password):
                self.add_error('password', forms.ValidationError(
                    "Password must contain at least one digit."))

            # Validate for special characters
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                self.add_error('password', forms.ValidationError(
                    "Password must contain at least one special character."))

        return cleaned_data

    def save(self, commit=True):
        """
        Saves the form data after setting the password using Django's built-in
        password hashing.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """
    A login form that accepts username and password, and validates the
    credentials using Django's authentication system.

    Fields:
        username: TextInput for the username.
        password: PasswordInput for the password.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and adds 'is-invalid' CSS class to fields with
        errors.
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'

    def clean(self):
        """
        Cleans the form and authenticates the user by checking the username
        and password.
        """
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                # Add error to both fields if authentication fails
                self.add_error('username', "Invalid Username or Password")
                self.add_error('password', "Invalid Username or Password")

        return cleaned_data


class BioForm(forms.ModelForm):
    """
    A form for updating the 'bio' field of the UserProfile model.

    Meta:
        model: UserProfile model.
        fields: Includes only the 'bio' field.
        widgets: Customizes the textarea widget for the 'bio' field.
    """
    class Meta:
        model = UserProfile
        fields = ('bio',)
        widgets = {
            'bio': forms.Textarea(
                attrs={'id': 'aboutme_textarea', 'class': 'form-control'}),
        }

    def clean_bio(self):
        """
        Cleans and normalizes the 'bio' field by removing extra spaces and
        ensuring its length does not exceed 1500 characters.
        """
        bio = self.cleaned_data.get('bio')

        if bio is not None:
            bio = re.sub(r'\s+', ' ', bio).strip()

            # Check length after normalization
            if len(bio) > 1500:
                self.add_error(
                    'bio', 'Bio cannot be longer than 1500 characters')

        return bio


class NewsletterForm(forms.ModelForm):
    """
    A form for newsletter signups, allowing users to submit their email
    address.

    Fields:
        user_email: Email field for the user's email address.
    """
    user_email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        })
    )

    class Meta:
        model = NewsletterSignup
        fields = ['user_email']

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and adds 'is-invalid' or 'is-valid' CSS class
        to fields based on validation results.
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'
            else:
                self.fields[field].widget.attrs['class'] += ' is-valid'

    def clean_user_email(self):
        """
        Cleans and validates the 'user_email' field by ensuring the email
        is not already signed up for the newsletter.
        """
        email = self.cleaned_data.get('user_email')
        if NewsletterSignup.objects.filter(user_email=email).exists():
            raise forms.ValidationError("This email is already signed up.")
        return email
