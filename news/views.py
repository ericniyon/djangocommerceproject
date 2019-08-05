from django.shortcuts import render, get_object_or_404
from .models import Album
# desplay the album with status 1 on my home page
def AlbumView(request):
    album = Album.objects.filter(status=1)
    context={
        'albums':album
    }
    template = 'album.html'
    return render(request, template, context)


#album detail views
def AlbumDetails(request, id):
    album_d = get_object_or_404(Album, pk=id)
    context = {
        'album_d':album_d
    }
    template = 'album_details.html'
    return render(request, template, context)