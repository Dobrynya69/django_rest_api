from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country/<pk>/', CountryAPIView.as_view()),
    path('', AllCountriesAPIView.as_view()),
]
