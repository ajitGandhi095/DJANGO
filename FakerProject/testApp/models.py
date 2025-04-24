from django.db import models

# Create your models here.
class STUDENT(models.Model):
    rollno= models.IntegerField()
    name= models.CharField(max_length=30)
    dob= models.DateField()
    marks= models.FloatField()
    email= models.CharField(max_length=50)
    phonenumber= models.BigIntegerField()
    address= models.TextField()