from django.shortcuts import render,redirect
from . form import MusicianForm
from .models import MusicianModel
# Create your views here.

def musician(request):
    if request.method=="POST":
        Musician = MusicianForm(request.POST)
        if Musician.is_valid():
            Musician.save()
            print(Musician.cleaned_data)
            return redirect("homepage")
    return render(request,'musician.html',{"Form":MusicianForm})

def EditMusician(request,id):
    MusicianObject = MusicianModel.objects.get(pk=id)
    EditMusicianForm = MusicianForm(instance=MusicianObject)
    if request.method=="POST":
        EditMusicianForm = MusicianForm(request.POST,instance=MusicianObject)
        if EditMusicianForm.is_valid():
            print(EditMusicianForm.cleaned_data)
            EditMusicianForm.save()
            return redirect('homepage')
    else:
        EditMusicianForm = MusicianForm(instance=MusicianObject)
    return render(request,'musician.html',{"Form":EditMusicianForm})