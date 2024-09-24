from django.shortcuts import render
from .models import About


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
    return render(request, 'home/home_page.html')
