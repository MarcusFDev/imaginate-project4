from django.shortcuts import render, redirect  # noqa
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .models import About
from .forms import RegistrationForm, LoginForm


def register_view(request):

    reg_form = RegistrationForm(request.POST)
    print("Registration Form Value:", reg_form)
    print("Registration Request:", request.method)

    if reg_form.is_valid():
        reg_form.save()
        username = reg_form.cleaned_data.get('username')
        password = reg_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            JsonResponse({'success': True})
            return render(request, "home/home.html")

        # If the form is invalid or the user couldn't be authenticated
        return JsonResponse(
            {'success': False, 'errors': reg_form.errors},
            status=400)

    # In case the request method is not POST
    return JsonResponse(
        {'success': False, 'error': 'Invalid request method'},
        status=405)


def login_view(request):

    login_form = LoginForm(request.POST)
    print("Login Form Value:", login_form)
    print("Login request:", request.method)

    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})

        # If the form is invalid or the user couldn't be authenticated
        return JsonResponse(
            {'success': False, 'errors': login_form.errors},
            status=400)

    # In case the request method is not POST
    return JsonResponse(
        {'success': False, 'error': 'Invalid request method'},
        status=405)


def handle_post(request):
    print("Post Detected.")
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'register':
            return register_view(request)

        elif form_type == 'login':
            return login_view(request)

    return JsonResponse(
        {'success': False, 'error': 'Invalid form type or request method'},
        status=400)


def user_profile(request):
    """
    Renders the User Profile page
    """
    about = About.objects.all().order_by('-updated_on').first()

    context = {
        "user": request.user,
        "about": about,
    }

    return render(
        request,
        "users/user_profile.html",
        context
    )


def home_page(request):

    reg_form = RegistrationForm()
    login_form = LoginForm()

    context = {
        "reg_form": reg_form,
        "login_form": login_form,
    }

    return render(
        request,
        'home/home_page.html',
        context
    )
