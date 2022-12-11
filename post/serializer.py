from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    is_liked = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated and obj.like_users.filter(pk=request.user.pk).exists():
            return True
        return False

    def get_like_count(self, obj):
        return obj.like_users.count()

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'melody', 'is_liked', 'like_count')
        read_only_fields = ('author', )
