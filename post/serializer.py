from rest_framework import serializers
from .models import Post, Tag
import re


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    is_liked = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    str_tags = serializers.CharField(max_length=60, write_only=True, allow_blank=True)

    def get_is_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated and obj.like_users.filter(pk=request.user.pk).exists():
            return True
        return False

    def get_like_count(self, obj):
        return obj.like_users.count()

    def create(self, validated_data):
        tag_names = validated_data.pop('str_tags')
        tag_names = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z#]", "", tag_names)    # 특수 문자 제거 (#제외)
        instance = super().create(validated_data)
        tags = []
        for name in tag_names.split('#')[1:]:   # '#'이 안붙은 태그는 제거
            if not name:
                continue    # 공백은 X
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        instance.tags.set(tags)
        return instance

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'melody', 'is_liked', 'like_count', 'tags', 'str_tags')
        read_only_fields = ('author', )
