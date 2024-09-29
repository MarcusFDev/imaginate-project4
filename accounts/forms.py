import re
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
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

    def clean_username(self):
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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        if password:
            if len(password) < 8 or len(password) > 20:
                raise forms.ValidationError(
                    "Password must be between 8 and 20 characters")

            if not re.search(r'\d', password):
                raise forms.ValidationError(
                    "Password must contain at least one digit.")
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                raise forms.ValidationError(
                    "Password must contain at least one special character.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
