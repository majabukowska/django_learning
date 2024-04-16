from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from .serializers import PostSerializer
from django.test import TestCase, override_settings
from .tasks import send_post_notification
from celery.contrib.testing.worker import start_worker
from myproject.celery import app

class PostTests(APITestCase):
    def test_view_posts(self):

        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):

        url = reverse('post-list')
        data = {'title': 'Test Title', 'content': 'Test content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_serializer_with_empty_data(self):
        serializer = PostSerializer(data={})
        self.assertFalse(serializer.is_valid())
