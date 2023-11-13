from django.shortcuts import render

def list_albums(request):
    return render(request, 'albums/index.html')
