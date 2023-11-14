from django import forms

class AlbumForm(forms.Form):
    album_title = forms.CharField(label='Album Title', max_length=150)
    artist_name = forms.CharField(label='Artist', max_length=150)
