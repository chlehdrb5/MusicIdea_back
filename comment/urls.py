from django.urls import path
from .views import CommentViewSet

urlpatterns = [
    path('<int:comment_id>', CommentViewSet.as_view(actions={
        'delete': 'destroy',
    })),
]
