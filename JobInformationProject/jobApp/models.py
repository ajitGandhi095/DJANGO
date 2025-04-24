from django.db import models

# Create your models here.
class HYD(models.Model):
    date= models.DateField()
    company = models.CharField(max_length=50)
    roll= models.CharField(max_length=40)
    eligibility= models.CharField(max_length=30)
    address= models.TextField()
    email= models.EmailField()
    phonenumber= models.BigIntegerField()

class PUNE(models.Model):
    date= models.DateField()
    company = models.CharField(max_length=50)
    roll= models.CharField(max_length=40)
    eligibility= models.CharField(max_length=30)
    address= models.TextField()
    email= models.EmailField()
    phonenumber= models.BigIntegerField()

class BANGALORE(models.Model):
    date= models.DateField()
    company = models.CharField(max_length=50)
    roll= models.CharField(max_length=40)
    eligibility= models.CharField(max_length=30)
    address= models.TextField()
    email= models.EmailField()
    phonenumber= models.BigIntegerField()