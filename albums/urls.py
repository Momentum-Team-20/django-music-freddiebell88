from django.urls import path
from . import views
# from .views import list_albums

urlpatterns = [
    path('', views.list_albums, name='home'),
]