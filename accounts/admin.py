from django.contrib import admin
from .models import UserProfile, NewsletterSignup
from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the UserProfile model, integrating the Summernote
    text editor for editing the 'bio' field.

    Attributes:
        summernote_fields: Specifies the fields to be edited
        using the editor.
        list_display: Defines the fields to be displayed in the list
        view in the Admin Panel ('user', 'bio', 'created_on', 'last_login').

    Media:
        css: Defines custom CSS files to be included in the admin for
        Summernote.
        js: Defines custom JavaScript files, including jQuery and
        Summernote initialization scripts, to be included in the admin.

    """

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
    """
    Admin configuration for the NewsletterSignup model.

    Attributes:
        list_display: Specifies the fields ('user_email', 'signup_data',
        'is_active') to be shown in the list view in the admin panel.
        list_filter: Adds filtering options based on the 'is_active' field.
        search_fields: Specifies 'user_email' as a searchable field
        within the admin.

    """

    list_display = ('user_email', 'signup_data', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user_email',)
