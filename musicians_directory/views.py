from django.shortcuts import render
from album.models import AlbumModel

def home(request):
    Albums = AlbumModel.objects.all()
    return render(request,'home.html',{"Albums":Albums})

