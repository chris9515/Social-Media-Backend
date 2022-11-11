from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    following = models.ManyToManyField('self', related_name='followers_set', blank=True, symmetrical=False)

    def get_followers(self):
        return self.following.all()

    def get_following(self):
        return self.followers_set.all()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def get_likes(self):
        return self.likes.all()

    def get_likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
