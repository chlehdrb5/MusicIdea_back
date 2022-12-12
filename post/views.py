from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from post.models import Post
from post.serializer import PostSerializer


class PostPagination(PageNumberPagination):
    page_size = 9


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

    filter_backends = [OrderingFilter]
    ordering_fields = []
    ordering = ['-id']

    lookup_url_kwarg = 'post_id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def like(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user.is_authenticated:
            if post.like_users.filter(pk=request.user.pk).exists():
                # 이미 해당 post에 좋아요를 누른 경우
                post.like_users.remove(request.user)
            else:
                # 좋아요를 누르면 추가
                post.like_users.add(request.user)
            post.save()

        return Response({"like_count": post.like_users.count()})
