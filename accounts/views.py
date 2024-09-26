from django.shortcuts import render, redirect
from django.contrib.auth.models import User # noqa
from .models import About
from .forms import RegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = RegistrationForm()

    return render(request, 'home/home_page.html', {'form': form})


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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = RegistrationForm()

    return render(request, 'home/home_page.html', {'form': form})
