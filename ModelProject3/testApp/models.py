from django.db import models

# Create your models here.
class Teacher(models.Model):
    tno= models.IntegerField()
    tname= models.CharField(max_length=30)
    sub= models.CharField(max_length=30)
    sal= models.FloatField()