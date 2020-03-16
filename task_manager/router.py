from .api.viewsets import TaskViewSet, TagViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('task-list', TaskViewSet, basename='task')
router.register('tag-list', TagViewSet)