from django.db import models
from musician.models import MusicianModel
# Create your models here.

class AlbumModel(models.Model):
    id = models.AutoField(primary_key=True)
    AlbumName = models.CharField(max_length=50)
    Singer = models.ForeignKey(MusicianModel,on_delete=models.CASCADE,default=1)
    AlbumReleaseDate = models.DateTimeField(auto_now_add=True)
    AlbumRating = [
        ("1",1),
        ("2",2),
        ("3",3),
        ("4",4),
        ("4",5),
    ]
    Rating = models.CharField(max_length=1,choices=AlbumRating,default=1)

    def __str__(self):
        return self.AlbumName