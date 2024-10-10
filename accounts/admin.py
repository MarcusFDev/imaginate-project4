from django.contrib import admin  # noqa
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
    list_display = ('title', 'acc_user')

    class Media:
        css = {
            'all': ('css/summernote.css',),
        }

        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'js/summernote.js',
            )
