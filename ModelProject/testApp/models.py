from django.db import models

# Create your models here.
class Employee(models.Model):
    Eno = models.IntegerField()
    Name = models.CharField(max_length=30)
    Sal = models.FloatField()
    Eaddr = models.CharField(max_length=30)