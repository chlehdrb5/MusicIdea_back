from django.db import models
from user.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    melody = models.TextField(null=False)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
