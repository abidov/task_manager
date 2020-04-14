from rest_framework import serializers
from task_manager.models import Task, Tag

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'date_of_creation', 'description', 'tags']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'date_of_creation', 'task']
