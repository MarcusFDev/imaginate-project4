from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Story


# Create your views here.
class StoryList(LoginRequiredMixin, generic.ListView):
    model = Story
    template_name = "stories/index.html"
    paginate_by = 15
    login_url = 'homepage'

    def get_queryset(self):
        queryset = Story.objects.filter(status=1, is_private=False)

        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        sort_filter = self.request.GET.get('sort', 'upvotes_desc')

        if sort_filter == 'upvotes_asc':
            queryset = queryset.order_by('upvotes')
        elif sort_filter == 'upvotes_desc':
            queryset = queryset.order_by('-upvotes')
        elif sort_filter == 'created_on_asc':
            queryset = queryset.order_by('created_on')
        elif sort_filter == 'created_on_desc':
            queryset = queryset.order_by('-created_on')

        return queryset


@login_required(login_url='homepage')
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
