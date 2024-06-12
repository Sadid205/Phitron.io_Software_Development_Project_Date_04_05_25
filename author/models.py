from django.db import models
from car.models import Car
from django.contrib.auth.models import User
# Create your models here.

class UserOrder(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car.title
    

