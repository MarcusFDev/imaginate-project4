from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import UserProfile
from .forms import RegistrationForm, LoginForm, BioForm


def register_view(request):
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
    print("Post Detected.")
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'register':
            return register_view(request)

        elif form_type == 'login':
            return login_view(request)


def user_profile(request):
    """
    Renders the User Profile page
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
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return render(request, 'accounts/home/home_page.html')
    return JsonResponse({'error': 'Account not found'}, status=400)


def home_page(request):

    reg_form = RegistrationForm()
    login_form = LoginForm()

    context = {
        "reg_form": reg_form,
        "login_form": login_form,
    }

    return render(
        request,
        'accounts/home/home_page.html',
        context
    )
