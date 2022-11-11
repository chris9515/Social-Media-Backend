from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import (
    User,
    Post,
)
from .permissions import IsAdminOrSelf
from .serializers import (
    UserSerializer,
    PostSerializer,
    CommentSerializer,
)


# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminOrSelf])
def follow(request, pk):
    query_user = User.objects.get(pk=pk)
    user = request.user
    user.following.add(query_user)
    return Response(
        {
            "message": "User followed",
            "following": user.following.count(),
            "followers": user.followers_set.count()
        }, status=200
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminOrSelf])
def unfollow(request, pk):
    query_user = User.objects.get(pk=pk)
    user = request.user
    user.following.remove(query_user)
    return Response(
        {
            "message": "User unfollowed",
            "following": user.following.count(),
            "followers": user.followers_set.count()
        }, status=200
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    user = request.user
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(
            {
                "message": "Post created",
                "post": serializer.data
            }, status=201
        )
    return Response(
        {
            "message": "Post not created",
            "errors": serializer.errors
        }, status=400
    )


@api_view(['DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def get_or_delete_post(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    if request.method == 'DELETE':
        if post.user == user:
            post.delete()
            return Response(
                {
                    "message": "Post deleted"
                }, status=200
            )
        return Response(
            {
                "message": "You are not authorized to delete this post"
            }, status=401
        )
    serializer = PostSerializer(post)
    return Response(
        {
            "post": serializer.data
        }, status=200
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    post.likes.add(user)
    return Response(
        {
            "message": "Post liked",
            "data": PostSerializer(post).data
        }, status=200
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    post.likes.remove(user)
    return Response(
        {
            "message": "Post unliked",
            "data": PostSerializer(post).data
        }, status=200
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_post(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user, post=post)
        return Response(
            {
                "message": "Comment created",
                "data": serializer.data
            }, status=201
        )
    return Response(
        {
            "message": "Comment not created",
            "errors": serializer.errors
        }, status=400
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_posts(request):
    user = request.user
    posts = user.posts.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(
        {
            "posts": serializer.data
        }, status=200
    )


