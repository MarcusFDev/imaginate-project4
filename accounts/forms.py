import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'
            else:
                self.fields[field].widget.attrs['class'] += ' is-valid'

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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email

    def clean(self):
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
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
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
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                self.add_error('username', "Invalid Username or Password")
                self.add_error('password', "Invalid Username or Password")

        return cleaned_data
