from django.urls import path
from .views import TaskListView, TaskCreateView, TagListView, TagCreateView, TaskDetailView, TagDetailView


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),

    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),

    path('tags/', TagListView.as_view(), name='tag-list'),

    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
]