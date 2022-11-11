from rest_framework import serializers

from api.models import (
    User,
    Post,
    Comment,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login', 'following', 'followers_set']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'created_at', 'updated_at', 'likes', 'comments']
        read_only_fields = ['user', 'created_at', 'updated_at', 'likes', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['user', 'post', 'created_at', 'updated_at']