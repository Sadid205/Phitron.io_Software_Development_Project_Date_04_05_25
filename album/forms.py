from django import forms 
from .models import Album
class Album_form(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        labels = {
            "AlbumName":"Album Name",
            "AlbumReleaseDate":"Album Release Date",
        }