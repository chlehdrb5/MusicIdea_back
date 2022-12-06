from django.urls import path

from .views import PostViewSet

urlpatterns = [
    path('<int:post_id>', PostViewSet.as_view(actions={
        'get': 'retrieve',
    })),
    # path('<int:post_id>/comments', CommentViewSet.as_view(actions={
    #     'get': 'list',
    #     'post': 'create',
    # })),
]
