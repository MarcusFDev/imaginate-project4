from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import UserProfile
from .forms import RegistrationForm, LoginForm, BioForm, NewsletterForm


def register_view(request):
    """
    Handles the registration of a new user. If the form is valid, the user is
    created and logged in automatically. If the form is invalid or
    authentication fails, the page is re-rendered with error messages.

    Args:
        request: The HTTP request object containing POST data from the
        registration form.

    Returns:
        HttpResponse: A rendered home page template with the registration form
        and potential error context.
    """
    reg_form = RegistrationForm(request.POST)

    context = {}

    if reg_form.is_valid():
        reg_form.save()

        username = reg_form.cleaned_data.get('username')
        password = reg_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "accounts/home/home_page.html")

    # If the form is invalid or the user couldn't be authenticated
    else:
        context['has_error'] = True
        context['reg_form'] = reg_form
        return render(
            request, 'accounts/home/home_page.html', context)


def login_view(request):
    """
    Handles user login. If the credentials are valid, the user is logged in
    and redirected to the home page. If login fails, the page is re-rendered
    with error messages.

    Args:
        request: The HTTP request object containing POST data from the login
        form.

    Returns:
        HttpResponse: A rendered home page template with the login form and
        potential error context.
    """
    login_form = LoginForm(request.POST)

    context = {}

    if login_form.is_valid():

        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "accounts/home/home_page.html")

    # If the form is invalid or the user couldn't be authenticated
    else:
        context['has_error'] = True
        context['login_form'] = login_form
        return render(
            request, 'accounts/home/home_page.html', context)


def handle_post(request):
    """
    Detects whether a POST request is for registration or login, and routes
    the request to the appropriate view.

    Args:
        request: The HTTP request object containing POST data.

    Returns:
        HttpResponse: A response from either the registration or login view,
        depending on the type of form submitted.
    """
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'register':
            return register_view(request)

        elif form_type == 'login':
            return login_view(request)


def user_profile(request):
    """
    Displays the current user's profile page, creating a UserProfile if one
    doesn't exist. The profile includes the bio and other user details.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A rendered user profile page template with the user's
        profile data in the context.
    """
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user)

    context = {
        "user_profile": user_profile,
        "profile_user": request.user,
        "bio": user_profile.bio,
        'profile_owner': True
    }

    return render(
        request,
        "accounts/users/user_profile.html",
        context
    )


def view_profile(request, username):
    """
    Displays a public profile page for a given username. The profile includes
    the user's bio and other details. If the logged-in user is viewing their
    own profile, they are marked as the profile owner.

    Args:
        request: The HTTP request object.
        username: The username of the profile to be viewed.

    Returns:
        HttpResponse: A rendered user profile page template with the user's
        profile data in the context.
    """

    profile_user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=profile_user)

    bio = user_profile.bio

    return render(request, 'accounts/users/user_profile.html', {
        'user_profile': user_profile,
        'profile_user': profile_user,
        "bio": bio,
        'profile_owner': request.user == profile_user,
    })


@login_required(login_url='homepage')
@require_POST
def update_bio(request):
    """
    Updates the bio of the logged-in user via a POST request. The bio is
    validated and saved if the form is valid.

    Args:
        request: The HTTP request object containing POST data with the updated
        bio.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = BioForm(request.POST, instance=user_profile)

        if form.is_valid():
            form.save()
            return JsonResponse(
                {'status': 'success', 'content': user_profile.bio})

    return JsonResponse(
        {'status': 'error', 'error': 'Invalid request'}, status=400)


@login_required(login_url='homepage')
def logout_account(request):
    """
    Logs out the current user via a POST request and returns a JSON response.

    Args:
        request: The HTTP request object, expected to be a POST request.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    if request.method == 'POST':
        logout(request)

        return JsonResponse({'success': True}, status=200)
    return JsonResponse({'error': 'Account not found'}, status=400)


@login_required(login_url='homepage')
def delete_account(request):
    """
    Deletes the current user's account via a POST request and logs them out.

    Args:
        request: The HTTP request object, expected to be a POST request.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()

        return JsonResponse({'success': 'Account deleted'}, status=200)
    return JsonResponse({'error': 'Account not found'}, status=400)


def home_page(request):
    """
    Renders the home page with registration, login, and newsletter subscription
    forms. Processes newsletter subscriptions via a POST request.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A rendered home page template with registration, login,
        and newsletter forms in the context.
    """
    reg_form = RegistrationForm()
    login_form = LoginForm()
    newsletter_form = NewsletterForm()

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(
                request, "Thank you for subscribing to our newsletter!")
            return redirect('homepage')
        else:
            messages.error(request, "There was a error with your submission.")

    context = {
        "reg_form": reg_form,
        "login_form": login_form,
        "newsletter_form": newsletter_form
    }

    return render(
        request,
        'accounts/home/home_page.html',
        context
    )
