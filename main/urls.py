from django.contrib import admin
from django.urls import path, include
from .views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('accounts/', include('allauth.urls')),
    path('api/', include('task_manager.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
]