from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task, Tag
from .permissions import IsOwner
from .serializers import TaskSerializer, TagSerializer

class TaskListView(generics.ListAPIView):
    """Task List View"""    
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Task Detail View"""
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self):
        obj = get_object_or_404(Task.objects.filter(user=self.request.user), pk=self.kwargs["pk"])
        return obj

class TaskCreateView(generics.CreateAPIView):
    """Task Create View"""    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagListView(generics.ListAPIView):
    """Tag List View"""    
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Tag Detail View"""
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self):
        obj = get_object_or_404(Tag.objects.filter(user=self.request.user), pk=self.kwargs["pk"])
        return obj

class TagCreateView(generics.CreateAPIView):
    """Tag Create View"""    
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)