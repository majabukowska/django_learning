from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .tasks import send_post_notification
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        post = self.get_object()
        post.is_archived = True
        post.save()
        return Response({'status': 'post archived'})

    def perform_create(self, serializer):
        post = serializer.save()
        send_post_notification.delay('majabukowska8@gmail.com', post.title)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.annotate(comments_count=Count('comments'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer