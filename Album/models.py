from django.db import models
from musician.models import musician

# Create your models here.


class Album(models.Model):
    Album_Name=models.CharField(max_length=50)
    Album_release_date=models.DateField()
    Rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    musician=models.ForeignKey(musician,on_delete=models.CASCADE )
    
    def __str__(self):

        return self.Album_Name
