from . import views
from django.urls import path


urlpatterns = [
    path('', views.StoryList.as_view(), name='home'),
    path('<slug:slug>/', views.story_page, name='story_page'),
]
