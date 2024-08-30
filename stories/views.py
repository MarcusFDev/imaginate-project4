from django.shortcuts import render # noqa
from django.views import generic
from .models import Story


# Create your views here.
class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "story_list.html"
