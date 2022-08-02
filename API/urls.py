from django.urls import path, include
from .views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country/<pk>/', CountryAPIView.as_view()),
    path('auth-dj/registration/', include('dj_rest_auth.registration.urls')),
    path('auth-dj/', include('dj_rest_auth.urls')),
    path('', AllCountriesAPIView.as_view()),
]
