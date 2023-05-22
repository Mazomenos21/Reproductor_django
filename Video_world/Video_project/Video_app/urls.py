from django.urls import path
from .views import home, videos,exit,buscar_videos

urlpatterns = [
   path('', home, name='home'),
   path('videos/', videos, name='videos'),
   path('logout/', exit, name='exit'),
   path('buscar_videos/', buscar_videos, name='buscar_videos'),
]
