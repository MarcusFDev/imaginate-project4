from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views import generic
from .models import Story, Comment
from .forms import StoryForm, CommentForm


# Create your views here.
class LibraryList(LoginRequiredMixin, generic.ListView):
    """
    Displays a paginated list of public stories that are not private.
    Search by title and sorting by upvotes or creation date.
    """
    model = Story
    template_name = "stories/index.html"
    paginate_by = 15
    login_url = 'homepage'

    def get_queryset(self):
        """
        Returns the queryset of public stories, filtered by search query and
        sorted based on user-selected criteria.

        Returns:
            QuerySet: The filtered and sorted list of stories.
        """
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


class MyStoryList(LoginRequiredMixin, generic.ListView):
    """
    Displays a paginated list of the current user's own stories.
    Supports optional search by title and sorting by upvotes or creation date.
    """
    model = Story
    template_name = "stories/my_stories.html"
    paginate_by = 15
    login_url = 'homepage'

    def get_queryset(self):
        """
        Returns the queryset of the user's own stories, filtered by search
        query and sorted based on user-selected criteria.

        Returns:
            QuerySet: The filtered and sorted list of the user's stories.
        """
        queryset = Story.objects.filter(status=1, author=self.request.user)

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
    Displays a specific story's page with associated comments.

    Args:
        request: The HTTP request object.
        slug: The slug of the story to retrieve.

    Returns:
        HttpResponse: A rendered story page template with the story and
        comments.
    """

    queryset = Story.objects.filter(status=1)
    story = get_object_or_404(queryset, slug=slug)

    comments = story.comments.all().order_by('-upvotes', 'created_on')
    comment_form = CommentForm()

    return render(
        request,
        "stories/story_page.html",
        {
            "story": story,
            "comments": comments,
            "comment_form": comment_form,
        }
    )


@login_required
def story_creator(request):
    """
    Handles story creation via a POST request. If the form is valid, the new
    story is saved. If the slug is a duplicate, a unique slug is generated.

    Args:
        request: The HTTP request object containing the story form data.

    Returns:
        HttpResponse: A redirect to the 'my_stories' page if successful,
        or re-renders the story creation page if the form is invalid.
    """

    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title']
            excerpt = form.cleaned_data['excerpt']
            content = form.cleaned_data['content']
            slug = slugify(title)
            author = request.user
            status = 1
            is_private = False

            # Check if the slug already exists
            if Story.objects.filter(slug=slug).exists():
                # If the slug already exists, append a number to the slug
                i = 1
                while Story.objects.filter(slug=f"{slug}-{i}").exists():
                    i += 1
                slug = f"{slug}-{i}"

            # Create a new Story instance
            Story.objects.create(
                title=title,
                slug=slug,
                author=author,
                content=content,
                excerpt=excerpt,
                status=status,
                is_private=is_private,
            )

            return redirect('my_stories')
        else:
            return render(
                request, 'stories/story_creator.html', {'form': form})
    else:
        form = StoryForm()
        return render(request, 'stories/story_creator.html', {'form': form})


@login_required(login_url='homepage')
@require_POST
def story_delete(request, slug):
    """
    Deletes a story if the current user is the author. Returns a JSON response
    with the success status or an error message if deletion fails.

    Args:
        request: The HTTP request object.
        slug: The slug of the story to delete.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    story = get_object_or_404(Story, slug=slug, author=request.user)

    try:
        if story.author == request.user:
            story.delete()
            return JsonResponse({'success': True, 'slug': slug})
        else:
            return JsonResponse(
                {'error': 'You do not have permission to delete this story'},
                status=403)

    except Story.DoesNotExist:
        return JsonResponse({'error': 'Story not found'}, status=404)


@login_required(login_url='homepage')
@require_POST
def story_private(request, slug):
    """
    Toggles a story's privacy status (public/private) and returns a JSON
    response indicating the new state.

    Args:
        request: The HTTP request object.
        slug: The slug of the story to update.

    Returns:
        JsonResponse: A JSON response with the updated privacy status.
    """
    story = get_object_or_404(Story, slug=slug, author=request.user)

    try:
        if story.is_private:
            story.is_private = False
            response_data = {
                'private': story.is_private,
                'action': 'Made public',
            }
        else:
            story.is_private = True
            response_data = {
                'private': story.is_private,
                'action': 'Made private',
            }

        story.save()

        return JsonResponse(response_data)

    except Story.DoesNotExist:
        return JsonResponse({'error': 'Story not found.'}, status=404)


@login_required(login_url='homepage')
@require_POST
def upvote_story(request, slug):
    """
    Upvotes or removes an upvote from a story. Returns a JSON response
    with the updated upvote count and the action taken.

    Args:
        request: The HTTP request object.
        slug: The slug of the story to upvote.

    Returns:
        JsonResponse: A JSON response with the new upvote count and action.
    """

    story = Story.objects.get(slug=slug)

    try:
        if story.upvoters.filter(id=request.user.id).exists():

            story.upvotes -= 1
            story.upvoters.remove(request.user)
            story.save()

            response_data = {
                'upvotes': story.upvotes,
                'action': 'removed',
            }

            return JsonResponse(response_data)

        story.upvotes += 1
        story.upvoters.add(request.user)
        story.save()

        response_data = {
            'upvotes': story.upvotes,
            'action': 'added',
        }

        return JsonResponse(response_data)

    except Story.DoesNotExist:
        return JsonResponse({'error': 'Story not found.'}, status=404)


@login_required(login_url='homepage')
def add_comment(request, slug):
    """
    Adds a new comment to a story if the request method is POST. Returns
    a JSON response indicating success or failure.

    Args:
        request: The HTTP request object containing the comment data.
        slug: The slug of the story to comment on.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """

    story = get_object_or_404(Story, slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.story = story
            new_comment.author = request.user
            new_comment.save()
            return JsonResponse({'success': 'Comment added'}, status=200)

    return JsonResponse({'error': 'Error adding comment'}, status=400)


@login_required(login_url='homepage')
@require_POST
def edit_comment(request, comment_id):
    """
    Edits a comment if the current user is the author. Returns a JSON response
    indicating success or failure.

    Args:
        request: The HTTP request object containing the edited comment data.
        comment_id: The ID of the comment to edit.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """

    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and comment.author == request.user:
            comment.body = form.cleaned_data['body']
            comment.save()

            return JsonResponse(
                {'message': 'Comment edited successfully'}, status=200)

    return JsonResponse({'message': 'Error editing comment'}, status=400)


@login_required(login_url='homepage')
@require_POST
def upvote_comment(request, comment_id):
    """
    Upvotes or removes an upvote from a comment. Returns a JSON response
    with the updated upvote count and the action taken.

    Args:
        request: The HTTP request object.
        comment_id: The ID of the comment to upvote.

    Returns:
        JsonResponse: A JSON response with the new upvote count and action.
    """

    comment = Comment.objects.get(id=comment_id)

    try:
        if comment.upvoters.filter(id=request.user.id).exists():

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

        response_data = {
            'upvotes': comment.upvotes,
            'action': 'added',
        }

        return JsonResponse(response_data)

    except Comment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found.'}, status=404)


@login_required(login_url='homepage')
@require_POST
def delete_comment(request, comment_id):
    """
    Deletes a comment if the current user is the author. Returns a JSON
    response indicating success or failure.

    Args:
        request: The HTTP request object.
        comment_id: The ID of the comment to delete.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """

    comment = Comment.objects.get(id=comment_id)

    try:
        if comment.author == request.user:
            comment.delete()
            return JsonResponse({'success': 'Comment deleted successfully'})
        else:
            return JsonResponse(
                {'error': 'You do not have permission to delete this comment'},
                status=403)

    except Comment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=404)


@login_required
def delete_all_stories(request):
    """
    Deletes all stories authored by the current user. Returns a JSON response
    indicating success or failure.

    Args:
        request: The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    if request.method == 'POST':
        stories = Story.objects.filter(author=request.user)
        if stories.exists():
            stories.delete()
            return JsonResponse({'success': True}, status=200)
        else:
            return JsonResponse({'error': 'No stories found'}, status=404)

    return JsonResponse({'error': 'No stories found'}, status=404)


@login_required
def delete_all_comments(request):
    if request.method == 'POST':
        comments = Comment.objects.filter(author=request.user)
        if comments.exists():
            comments.delete()
            return JsonResponse({'success': True}, status=200)
        else:
            return JsonResponse({'error': 'No comments found'}, status=404)

    return JsonResponse({'error': 'No comments found'}, status=404)
