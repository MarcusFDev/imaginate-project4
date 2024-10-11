from . import views
from django.urls import path


urlpatterns = [
    path('story/<slug:slug>/edit/', views.story_edit, name='story_edit'),
    path('story/<slug:slug>/delete/', views.story_delete, name='story_delete'),
    path(
        'delete-all-comments/',
        views.delete_all_comments, name='delete_all_comments'),
    path(
        'delete-all-stories/',
        views.delete_all_stories, name='delete_all_stories'),
    path(
        'edit-comment/<int:comment_id>/edit/',
        views.edit_comment, name='edit_comment'),
    path(
        'delete-comment/<int:comment_id>/',
        views.delete_comment, name='delete_comment'),
    path(
        'upvote-comment/<int:comment_id>/',
        views.upvote_comment, name='upvote_comment'),
    path(
        'story/<slug:slug>/add_comment/',
        views.add_comment, name='add_comment'),
    path(
        'story/<slug:slug>/upvote/',
        views.upvote_story, name='upvote_story'),
    path('my-stories/', views.MyStoryList.as_view(), name='my_stories'),
    path('', views.LibraryList.as_view(), name='library'),
    path('<slug:slug>/', views.story_page, name='story_page'),
]
