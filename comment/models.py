from django.db import models

# Create your models here.
from post.models import Post
from user.models import User


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.content}'
