from django.contrib import admin  # noqa
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):

    summernote_fields = ('bio',)
    list_display = ('user', 'bio', 'created_on', 'last_login')

    class Media:
        css = {
            'all': ('css/summernote.css',),
        }

        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'js/summernote.js',
            )
