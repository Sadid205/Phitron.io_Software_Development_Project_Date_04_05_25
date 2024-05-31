from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumModel

from musician.form import MusicianForm
from musician.models import MusicianModel

# Create your views here.

def Album(request):
    if request.method=="POST":
        Album = AlbumForm(request.POST)
        if Album.is_valid():
            Album.save()
            return redirect("homepage")
    else:
        Album = AlbumForm()
    return render(request,'album.html',{"Form":AlbumForm})



def Edit(request,id):
    AlbumObjects = AlbumModel.objects.get(pk=id)
    EditAlbum = AlbumForm(instance=AlbumObjects)
    if request.method=="POST":
        EditAlbum = AlbumForm(request.POST,instance=AlbumObjects)
        if EditAlbum.is_valid():
            EditAlbum.save()
            print(EditAlbum.cleaned_data)
            return redirect("homepage")
    else:
        EditAlbum=AlbumForm(instance=AlbumObjects)
    return render(request,'album.html',{"Form":EditAlbum})

def DeleteAlbum(request,id):
    AlbumObjects = AlbumModel.objects.get(pk=id)
    AlbumObjects.delete()
    return redirect('homepage')