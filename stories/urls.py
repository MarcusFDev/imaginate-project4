from . import views
from django.urls import path


urlpatterns = [
    path('stories', views.StoryList.as_view(), name='stories'),
    path('<slug:slug>/', views.story_page, name='story_page'),
]
