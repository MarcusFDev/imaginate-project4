from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile/', views.user_profile, name='user_profile'),
]
