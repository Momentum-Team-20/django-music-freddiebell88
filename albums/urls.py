from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='home'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albums/new/', views.create_album, name='new'),
    path('albums/<int:pk>/delete', views.delete_album, name='delete'),
    path('albums/<int:pk>/edit', views.edit_album, name='edit'),
]
