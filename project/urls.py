from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')),
    path('admin_framework/', include('rest_framework.urls')),
]
