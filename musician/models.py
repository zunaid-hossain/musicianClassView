from django.db import models
# Create your models here.

class musician(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name =models.CharField(max_length=50)
    Email=models.EmailField()
    Phone_number=models.IntegerField()
    Instrument_Type=models.CharField(max_length=50)
    
    def __str__(self):

        return self.First_Name+" "+self.Last_Name


