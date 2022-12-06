from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from comment.models import Comment
from comment.serializer import CommentSerializer
from post.models import Post


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        if 'post_id' in self.kwargs:
            post_id = self.kwargs['post_id']
            return Comment.objects.filter(post_id=post_id)
        else:
            return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        serializer.save(post=post)
