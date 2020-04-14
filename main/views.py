from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy


@api_view(['GET'])
def api_root(request):
    response = Response({
        'task-list': reverse_lazy('task-list', request=request),
        'task-create': reverse_lazy('task-create', request=request),
        'tag-list': reverse_lazy('tag-list', request=request),
        'tag-create': reverse_lazy('tag-create', request=request),
        'rest_login': reverse_lazy('rest_login', request=request),
        'rest_logout': reverse_lazy('rest_logout', request=request),
        'rest_register': reverse_lazy('rest_register', request=request),
    })
    return response