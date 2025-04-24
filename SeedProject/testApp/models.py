from django.db import models

# Create your models here.

class Employee(models.Model):
    eno= models.IntegerField()
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=40)
    dsg= models.CharField(max_length=30)
    phonenumber= models.BigIntegerField()
    address= models.TextField()