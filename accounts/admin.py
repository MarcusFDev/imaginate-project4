from django.contrib import admin  # noqa
from .models import UserProfile, NewsletterSignup
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


@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'signup_data', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user_email',)
