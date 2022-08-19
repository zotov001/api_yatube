from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

from posts.models import Comment, Group, Post
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from api.permissions import UserIsAuthor


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с комментариями."""
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, UserIsAuthor)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        new_queryset = Comment.objects.filter(post=post)
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для работы с группами."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с постами."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, UserIsAuthor)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
