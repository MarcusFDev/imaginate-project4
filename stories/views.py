from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Story


# Create your views here.
class StoryList(generic.ListView):
    queryset = Story.objects.filter(status=1, is_private=False)
    template_name = "stories/index.html"
    paginate_by = 15


def story_page(request, slug):
    """
    Display an individual :model:`stories.Story`.

    **Context**

    ``post``
        An instance of :model:`stories.Story`.

    **Template:**

    :template:`stories/story_page.html`
    """

    queryset = Story.objects.filter(status=1)
    story = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "stories/story_page.html",
        {"story": story},
    )
