from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Task, Tag

from .api.serializers import TaskSerializer, TagSerializer

class TaskViewTestCase(APITestCase):
    list_url = reverse('task-list')
    def setUp(self):
        Task.objects.create(name='TestCase', description='TestCase')

    def test_task_create(self):
        response = self.client.post(self.list_url, data={'name': 'TestCase', 'description': 'TestCase'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_task_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail(self):
        task = Task.objects.first()
        response = self.client.get(task.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TagViewTestCase(APITestCase):
    list_url = reverse('tag-list')
    def setUp(self):
        Tag.objects.create(name='TestCase')

    def test_tag_create(self):
        response = self.client.post(self.list_url, data={'name': 'TestCase'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tag_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_detail(self):
        tag = Tag.objects.first()
        response = self.client.get(tag.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)