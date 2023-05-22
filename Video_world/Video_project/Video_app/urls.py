from django.urls import path
from .views import home, videos,exit

urlpatterns = [
   path('', home, name='home'),
   path('videos/', videos, name='videos'),
   path('logout/', exit, name='exit'),
]
