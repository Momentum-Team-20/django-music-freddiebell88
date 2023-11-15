from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Album
from django.views import generic
from .forms import AlbumForm

# home page list of all albums
def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})

# detail page for specific album
class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'albums/album_detail.html'

# add an album to the list/database
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'albums/new.html', {'form': form})


# delete an album from list/database
def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    album.delete()
    return redirect('home')


# update an existing album
def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        
