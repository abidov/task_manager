from django.urls import path
from .api.viewsets import TaskViewSet, TagViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from .views import api_root


urlpatterns = format_suffix_patterns([
    path('', api_root, name='api-root'),

    path('tasks/',
         TaskViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='task-list'),

    path('tasks/<int:pk>/',
         TaskViewSet.as_view({'get': 'retrieve', 'put': 'update',}),
         name='task-detail'),

    path('tags/',
         TagViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='tag-list'),

    path('tags/<int:pk>/',
         TagViewSet.as_view({'get': 'retrieve', 'put': 'update',}),
         name='tag-detail'),
])
