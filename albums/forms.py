from django import forms
from django.forms import ModelForm
from .models import Album


class AlbumForm(ModelForm):
    title = forms.CharField(max_length=250)
    artist_name = forms.CharField(max_length=250)

    class Meta:
        model = Album
        fields = ['title', 'artist_name', 'image']

