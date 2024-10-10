from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import About
from .forms import RegistrationForm, LoginForm, AboutForm


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
            return render(request, "home/home_page.html")

    # If the form is invalid or the user couldn't be authenticated
    else:
        context['has_error'] = True
        context['reg_form'] = reg_form
        return render(
            request, 'home/home_page.html', context)


def login_view(request):
    login_form = LoginForm(request.POST)

    context = {}

    if login_form.is_valid():

        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "home/home_page.html")

    # If the form is invalid or the user couldn't be authenticated
    else:
        context['has_error'] = True
        context['login_form'] = login_form
        return render(
            request, 'home/home_page.html', context)


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


@login_required(login_url='homepage')
@require_POST
def add_about_description(request):

    if request.method == 'POST':
        form = AboutForm(request.POST)

        if form.is_valid():
            # Retrieve all About objects for the user
            about_entries = About.objects.filter(acc_user=request.user)

            if about_entries.exists():
                if about_entries.count() > 1:

                    about_entries.exclude(pk=about_entries.first().pk).delete()

                # Use the remaining object
                about = about_entries.first()
            else:
                # Create a new About object if none exist
                about = About.objects.create(acc_user=request.user)

            # Update the About object with the new content
            about.title = "About " + request.user.username
            about.content = form.cleaned_data['content']
            about.save()

            return JsonResponse(
                {'status': 'success', 'content': about.content})

        # Return error if the form is invalid
        return JsonResponse(
            {'status': 'error', 'error': 'Invalid request'}, status=400)


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
