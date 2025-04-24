import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FakerProject.settings')

import django
django.setup()

from random import *
from faker import Faker
fake= Faker()
from testApp.models import STUDENT

def phonenumbergen():
    d1= randint(6,9)
    num= '' + str(d1)
    for val in range(9):
        num += str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        frollno= fake.random_int(min=1, max=999)
        fname= fake.name()
        fdob= fake.date()
        fmarks= fake.random_int(min=0, max=100)
        femail= fake.email()
        fphonenumber= phonenumbergen()
        faddress= fake.address()
        STUDENT.objects.get_or_create(rollno=frollno, name=fname, dob=fdob, marks=fmarks, email=femail, phonenumber=fphonenumber, address=faddress)

n=int(input("Enter how many records um want to generate: "))
populate(n)
print(f"{n} records generated successfully.....")

    
