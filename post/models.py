import os
import uuid
from datetime import datetime

from django.db import models
from user.models import User
# Create your models here.


def file_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    d = datetime.now()
    filepath = d.strftime("%Y/%m/%d")
    suffix = d.strftime("%Y%m%d%H%M%S")
    filename = "%s_%s.%s" % (uuid.uuid4().hex, suffix, ext)
    return os.path.join(filepath, filename)


class Post(models.Model):
    title = models.CharField(null=False, max_length=50)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    melody = models.FileField(upload_to=file_upload_path, null=False)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_posts')
    tags = models.ManyToManyField('Tag', blank=True, related_name='post')

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    name = models.CharField(null=False, max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'
