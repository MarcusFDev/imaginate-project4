from django.shortcuts import render, redirect  # noqa
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .models import About
from .forms import RegistrationForm, LoginForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True})

        return JsonResponse({'success': False})

    return JsonResponse(
        {'success': False}, status=405)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('stories')
    else:
        form = LoginForm()

    return render(request, 'home', {'form': form})


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
    form = RegistrationForm()
    return render(request, 'home/home_page.html', {'form': form})
