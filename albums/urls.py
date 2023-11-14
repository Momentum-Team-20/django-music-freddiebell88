from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='home'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail')
]
