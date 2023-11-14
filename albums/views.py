from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Album
from django.views import generic
from .forms import AlbumForm


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})


# def album_detail(request):
    return render(request, 'album_detail.html')


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'albums/album_detail.html'


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
    else:
        form = AlbumForm
    return render(request, 'albums/new_album.html', {'form': form})
