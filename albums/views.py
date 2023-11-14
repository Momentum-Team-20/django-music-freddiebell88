from django.shortcuts import render
from .models import Album
from django.views import generic


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})


# def album_detail(request):
    return render(request, 'album_detail.html')


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'albums/album_detail.html'
