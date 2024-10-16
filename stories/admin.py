from django.contrib import admin
from .models import Story, Comment
from django_summernote.admin import SummernoteModelAdmin


class UpvoteRangeFilter(admin.SimpleListFilter):
    """
    A custom admin filter for filtering Story objects by their upvote range.

    Provides options to filter stories with the following upvote ranges:
        - 0 to 10 upvotes
        - 11 to 50 upvotes
        - 51 to 100 upvotes
        - 100+ upvotes

    Methods:
        lookups: Returns the list of upvote range options displayed in the
        admin.
        queryset: Filters the queryset based on the selected upvote range.
    """
    title = 'Upvotes'
    parameter_name = 'upvotes_range'

    def lookups(self, request, model_admin):
        """
        Defines the lookup options for filtering by upvote ranges.

        Returns:
            A list of tuples where each tuple represents a filter option.
        """
        return [
            ('0-10', '0 to 10'),
            ('11-50', '11 to 50'),
            ('51-100', '51 to 100'),
            ('100+', '100+'),
        ]

    def queryset(self, request, queryset):
        """
        Filters the queryset based on the selected upvote range.

        Args:
            request: The HTTP request object.
            queryset: The original queryset of stories.

        Returns:
            The filtered queryset based on the selected upvote range, or
            the original queryset if no filter is selected.
        """
        if self.value() == '0-10':
            return queryset.filter(upvotes__range=(0, 10))
        if self.value() == '11-50':
            return queryset.filter(upvotes__range=(11, 50))
        if self.value() == '51-100':
            return queryset.filter(upvotes__range=(51, 100))
        if self.value() == '100+':
            return queryset.filter(upvotes__gte=100)
        return queryset


@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):
    """
    Admin interface customization for the Story model.

    Customizations:
        - list_display: Specifies the fields displayed in the admin story list
          view.
        - search_fields: Adds a search bar that searches stories by title and
          author's username.
        - list_filter: Adds filters for story status, creation date, privacy,
          and upvote range.
        - prepopulated_fields: Automatically fills in the 'slug' field based
          on the 'title'.
        - summernote_fields: Specifies the content field to use the Summernote
          editor for rich text input.
    """

    list_display = ('title', 'slug', 'author', 'upvotes', 'is_private',
                    'status', 'created_on',)
    search_fields = ['title', 'author__username']
    list_filter = ('status', 'created_on', 'is_private', UpvoteRangeFilter)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
