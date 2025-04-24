from django.db import models

# Create your models here.
class Employee(models.Model):
    eno= models.IntegerField()
    ename= models.CharField(max_length=40)
    email= models.CharField(max_length=40, unique=True)
    deg= models.CharField(max_length=30)