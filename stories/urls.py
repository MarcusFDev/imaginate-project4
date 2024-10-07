from . import views
from django.urls import path


urlpatterns = [
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
    path('', views.StoryList.as_view(), name='stories'),
    path('<slug:slug>/', views.story_page, name='story_page'),
]
