from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_url_kwarg = 'post_id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)