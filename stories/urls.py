from . import views
from django.urls import path


urlpatterns = [
    path('delete-comment/', views.delete_comment, name='delete_comment'),
    path('upvote-comment/', views.upvote_comment, name='upvote_comment'),
    path('', views.StoryList.as_view(), name='stories'),
    path('<slug:slug>/', views.story_page, name='story_page'),
]
