from django.shortcuts import render
from album.models import Album

def home(request):
    Albums = Album.objects.all()
    return render(request,'home.html',{"Albums":Albums,'Title':'Home Page'})