from django import forms
from .models import Comment, Story
from django.utils.html import strip_tags


class CommentForm(forms.ModelForm):
    """
    A form for submitting or editing a comment related to a story.

    Fields:
        body: TextArea for the comment text, with a placeholder and a
        character limit of 500.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 1, 'placeholder': 'Add a comment...'}),
        }

    def clean(self):
        """
        Cleans and validates the 'body' field by checking:
        - Length: Ensures the comment is no more than 500 characters.
        """
        cleaned_data = super().clean()
        comment = cleaned_data.get('body')

        if comment and len(comment) > 500:
            self.add_error('body', "Comments are a Maximum of 500 characters.")

        return cleaned_data


class StoryForm(forms.ModelForm):
    """
    A form for creating or editing a story with title, excerpt, and content
    fields.

    Fields:
        title: TextInput for the story title with a placeholder and character
        limit.
        excerpt: TextArea for the story excerpt with a placeholder and
        character limit.
        content: TextArea for the main story content with a placeholder.
    """

    class Meta:
        model = Story
        fields = ('title', 'excerpt', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control story-editor-field',
                'placeholder': 'Enter story title',
            }),
            'excerpt': forms.Textarea(attrs={
                'id': 'id_excerpt',
                'class': 'form-control story-editor-excerpt summernote',
            }),
            'content': forms.Textarea(attrs={
                'id': 'id_content',
                'class': 'form-control story-editor-field summernote',
            }),
        }

    def clean_title(self):
        """
        Validates the 'title' field by ensuring:
        - The title is not empty.
        - The title does not exceed 50 characters.
        """
        title = self.cleaned_data.get('title')
        if not title or title.isspace():
            self.add_error(
                'title', "Title cannot be empty."
            )
        elif len(title) > 50:
            self.add_error(
                'title', "Title must be no more than 50 characters long.")
        return title

    def clean_excerpt(self):
        """
        Validates the 'excerpt' field by:
        - Stripping HTML tags.
        - Ensuring the excerpt is not empty.
        - Limiting the length to 500 characters.
        """
        excerpt = self.cleaned_data.get('excerpt')
        excerpt = strip_tags(excerpt)
        if not excerpt or excerpt.isspace():
            self.add_error(
                'excerpt', 'Excerpt cannot be empty.'
            )
        elif len(excerpt) > 500:
            self.add_error(
                'excerpt', "Excerpt must be no more than 500 characters long.")
        return excerpt

    def clean_content(self):
        """
        Validates the 'content' field by:
        - Stripping HTML tags.
        - Ensuring the content is not empty.
        """
        content = self.cleaned_data.get('content')
        content = strip_tags(content)
        if not content or content.isspace():
            self.add_error('content', "Content cannot be empty.")
        return content
