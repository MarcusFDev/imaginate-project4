from . import views
from django.urls import path
from .views import register_view, login_view


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile/', views.user_profile, name='user_profile'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
