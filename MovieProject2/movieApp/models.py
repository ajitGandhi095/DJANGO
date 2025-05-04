from django.db import models

# Create your models here.

class MovieModel(models.Model):
    title= models.CharField(max_length=30)
    hero= models.CharField(max_length=30)
    heroine= models.CharField(max_length=30)
    release= models.DateField()