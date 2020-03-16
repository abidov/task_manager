from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse


@api_view(['GET'])
def api_root(request):
    return Response({
        'task-list': request.build_absolute_uri(reverse('task-list')),
        'tag-list': request.build_absolute_uri(reverse('tag-list')),
    })