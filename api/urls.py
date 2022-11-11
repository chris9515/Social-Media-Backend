from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("follow/<int:pk>/", views.follow, name="follow"),
    path("unfollow/<int:pk>/", views.unfollow, name="unfollow"),

    path('user/', views.get_user, name='get_user'),
    path('posts/', views.create_post, name='create_post'),
    path('posts/<int:pk>/', views.get_or_delete_post, name='get_or_delete_post'),
    path('all_posts/', views.get_user_posts, name='get_post'),

    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('unlike/<int:pk>/', views.unlike_post, name='unlike_post'),

    path('comment/<int:pk>/', views.comment_post, name='create_comment'),

]

