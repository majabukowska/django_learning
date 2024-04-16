from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.test import TestCase, override_settings
from .tasks import send_post_notification
from celery.contrib.testing.worker import start_worker
from myproject.celery import app

class PostModelTests(TestCase):
    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)

class PostViewSetTests(APITestCase):
    def test_view_posts(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('post-list')
        data = {'title': 'Test Title', 'content': 'Test contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest contentTest content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_serializer_with_empty_data(self):
        serializer = PostSerializer(data={})
        self.assertFalse(serializer.is_valid())

class CommentModelTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Sample post", content="Sample content")

    def test_comment_creation(self):
        comment = Comment.objects.create(post=self.post, content="A sample comment")
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(str(comment), comment.content)

class CommentViewSetTests(APITestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Sample post", content="Sample content")

    def test_create_comment(self):
        url = reverse('comment-list')
        data = {'post': self.post.id, 'content': 'A sample comment'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CeleryTasksTest(TestCase):
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_send_post_notification(self):
        task = send_post_notification.delay('example@example.com', 'Test Title')
        self.assertTrue(task.successful())
