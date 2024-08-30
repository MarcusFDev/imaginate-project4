from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Story(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="story_entries"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    is_private = models.BooleanField(default=True)
    upvotes = models.IntegerField(default=0)

    class Meta:
        ordering = ["upvotes", 'created_on']

    def __str__(self):
        return (f"{self.title} | {self.upvotes} Upvotes |"
                f" written by {self.author}")


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`imaginate.Story`.
    """
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)

    class Meta:
        ordering = ["upvotes", 'created_on']

    def __str__(self):
        return (f"Comment | {self.body} | {self.upvotes} Upvotes |"
                f" by {self.author}")
