from django.contrib import admin
from .models import Story, Comment
from django_summernote.admin import SummernoteModelAdmin


class UpvoteRangeFilter(admin.SimpleListFilter):
    title = 'Upvotes'
    parameter_name = 'upvotes_range'

    def lookups(self, request, model_admin):
        return [
            ('0-10', '0 to 10'),
            ('11-50', '11 to 50'),
            ('51-100', '51 to 100'),
            ('100+', '100+'),
        ]

    def queryset(self, request, queryset):
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

    list_display = ('title', 'slug', 'author', 'upvotes', 'is_private',
                    'status', 'created_on',)
    search_fields = ['title', 'author__username']
    list_filter = ('status', 'created_on', 'is_private', UpvoteRangeFilter)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
