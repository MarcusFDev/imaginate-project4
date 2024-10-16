from django.urls import path
from .views import (
    home_page, handle_post, user_profile, update_bio, view_profile,
    delete_account, logout_account)


urlpatterns = [
    path('', home_page, name='home_page'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/<str:username>/', view_profile, name='view_profile'),
    path('register/', handle_post, name='register'),
    path('login/', handle_post, name='login'),
    path('update_bio/', update_bio, name='update_bio'),
    path('delete_account/', delete_account, name='delete_account'),
    path('logout_account/', logout_account, name='logout_account')
]
