from . import views
from django.urls import path
from .views import handle_post, add_about_description


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile/', views.user_profile, name='user_profile'),
    path('register/', handle_post, name='register'),
    path('login/', handle_post, name='login'),
    path('about/', add_about_description, name='about'),
]
