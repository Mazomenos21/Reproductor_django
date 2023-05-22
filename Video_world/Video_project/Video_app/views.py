from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Video
from django.db.models import Q


def home(request):
    return render(request, 'core/home.html')


@login_required
def videos(request):
    video = Video.objects.all()
    return render(request, 'core/videos.html', {'video': video})


def exit(request):
    logout(request)
    return redirect('home')

@login_required
def buscar_videos(request):
    busqueda = request.GET.get('buscar', '')
    videos = Video.objects.all()
    if busqueda:
        videos = videos.filter(
            Q(caption__icontains=busqueda) |
            Q(name__icontains=busqueda) |
            Q(video__icontains=busqueda) |
            Q(miniatura__icontains=busqueda)
        ).distinct()
    return render(request, 'core/listar_videos.html', {'video': videos})