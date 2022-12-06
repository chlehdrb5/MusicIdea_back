from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'melody')
        read_only_fields = ('author', )
