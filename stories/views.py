from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views import generic
from .models import Story, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 1, 'placeholder': 'Add a comment...'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        comment = cleaned_data.get('body')

        if comment and len(comment) > 500:
            self.add_error('body', "Comments are a Maximum of 500 characters.")

        return cleaned_data


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

    comments = story.comments.all().order_by('-upvotes', 'created_on')
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            return redirect('home')

        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.story = story
            new_comment.author = request.user
            new_comment.save()
            return redirect('story_page', slug=story.slug)

    return render(
        request,
        "stories/story_page.html",
        {
            "story": story,
            "comments": comments,
            "comment_form": comment_form,
        }
    )


@login_required(login_url='homepage')
@require_POST
def upvote_comment(request):

    comment_id = request.POST.get('comment_id')
    comment = Comment.objects.get(id=comment_id)

    try:
        if comment.upvoters.filter(id=request.user.id).exists():
            # User has already upvoted, remove the upvote
            comment.upvotes -= 1
            comment.upvoters.remove(request.user)
            comment.save()

            response_data = {
                'upvotes': comment.upvotes,
                'action': 'removed',
            }

            return JsonResponse(response_data)

        comment.upvotes += 1
        comment.upvoters.add(request.user)
        comment.save()

        # Prepare JSON response
        response_data = {
            'upvotes': comment.upvotes,
            'action': 'added',
        }

        return JsonResponse(response_data)

    except Comment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found.'}, status=404)
