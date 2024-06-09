from django.db import models

# Create your models here.

class musician(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=11)
    InstrumentType = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
