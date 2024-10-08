from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1500, blank=True)
    profile_picture = models.ImageField(
        default='static/images/default-user-icon.webp')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Profile"
