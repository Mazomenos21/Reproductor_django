from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Video


def home(request):
    return render(request, 'core/home.html')


@login_required
def videos(request):
    video=Video.objects.all()
    return render(request, 'core/videos.html', {'video': video})


def exit(request):
    logout(request)
    return redirect('home')
