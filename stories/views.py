from django.shortcuts import render # noqa
from django.http import HttpResponse


# Create your views here.
def my_story(request):
    return HttpResponse("Hello, this will be the main story page!")
