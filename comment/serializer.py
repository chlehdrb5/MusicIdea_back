from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content']
        read_only_fields = ('post', 'author')
