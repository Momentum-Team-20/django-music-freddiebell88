from django.shortcuts import render
from .models import Album


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})
