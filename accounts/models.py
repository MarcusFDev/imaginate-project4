from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1500)
    acc_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
