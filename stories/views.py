from django.shortcuts import render # noqa
from django.views import generic
from .models import Story


# Create your views here.
class StoryList(generic.ListView):
    queryset = Story.objects.filter(status=1, is_private=False)
    template_name = "stories/index.html"
    paginate_by = 15
