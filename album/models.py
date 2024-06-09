from django.db import models
from musician.models import musician
# Create your models here.

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    AlbumName = models.CharField(max_length=50)
    Singer = models.ForeignKey(musician,on_delete=models.CASCADE)
    AlbumReleaseDate = models.DateTimeField(auto_now_add=True)
    Field_choices = [
        ("1",1),
        ("2",2),
        ("3",3),
        ("4",4),
        ("5",5),
    ]
    Rating = models.CharField(max_length=1,choices=Field_choices,default=1)