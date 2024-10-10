from django.urls import path
from .views import (
    home_page, handle_post, user_profile, update_bio, view_profile)


urlpatterns = [
    path('', home_page, name='home_page'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/<str:username>/', view_profile, name='view_profile'),
    path('register/', handle_post, name='register'),
    path('login/', handle_post, name='login'),
    path('update_bio/', update_bio, name='update_bio'),
]
