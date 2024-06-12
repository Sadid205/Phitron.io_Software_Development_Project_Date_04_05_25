from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=40)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self.name}"