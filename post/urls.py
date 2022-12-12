from django.urls import path

from comment.views import CommentViewSet
from .views import PostViewSet

urlpatterns = [
    path('<int:post_id>', PostViewSet.as_view(actions={
        'get': 'retrieve',
        'delete': 'destroy',
    })),
    path('<int:post_id>/like', PostViewSet.as_view(actions={
        'get': 'like',
    })),
    path('<int:post_id>/comment', CommentViewSet.as_view(actions={
        'post': 'create',
    })),
    path('<int:post_id>/comments', CommentViewSet.as_view(actions={
        'get': 'list',
    })),
]
