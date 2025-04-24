import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JobInformationProject.settings')

import django
django.setup()

from jobApp.models import HYD,PUNE,BANGALORE
from random import *
from faker import Faker
fake= Faker()

def phonenumbergen():
    d1= randint(6,9)
    num= '' + str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)

def hyd_populate(n):
    for i in range(n):
        fdate= fake.date()
        fcompany= fake.company()
        froll= fake.random_element(elements=("Project Manager", "Team Lead", "Software Developer", "Software Tester", "Associate Software Engineer"))
        feligibility= fake.random_element(elements=("B.Tech", "Bsc", "M.Tech", "MCA", "BCA", "Phd", "Mahesh sir Student"))
        femail= fake.email()
        faddress= fake.address()
        fphonenumber= phonenumbergen()
        hyd_jobs_record = HYD.objects.get_or_create(
            date=fdate, 
            company=fcompany, 
            roll=froll, 
            eligibility=feligibility, 
            email= femail,
            address=faddress, 
            phonenumber=fphonenumber
        )

def pune_populate(n):
    for i in range(n):
        fdate= fake.date()
        fcompany= fake.company()
        froll= fake.random_element(elements=("Project Manager", "Team Lead", "Software Developer", "Software Tester", "Associate Software Engineer"))
        feligibility= fake.random_element(elements=("B.Tech", "Bsc", "M.Tech", "MCA", "BCA", "Phd", "Mahesh sir Student"))
        femail= fake.email()
        faddress= fake.address()
        fphonenumber= phonenumbergen()
        pune_jobs_record = PUNE.objects.get_or_create(
            date=fdate, 
            company=fcompany, 
            roll=froll, 
            eligibility=feligibility, 
            email= femail,
            address=faddress, 
            phonenumber=fphonenumber
        )

def banglore_populate(n):
    for i in range(n):
        fdate= fake.date()
        fcompany= fake.company()
        froll= fake.random_element(elements=("Project Manager", "Team Lead", "Software Developer", "Software Tester", "Associate Software Engineer"))
        feligibility= fake.random_element(elements=("B.Tech", "Bsc", "M.Tech", "MCA", "BCA", "Phd", "Mahesh sir Student"))
        femail= fake.email()
        faddress= fake.address()
        fphonenumber= phonenumbergen()
        banglore_jobs_record = BANGALORE.objects.get_or_create(
            date=fdate, 
            company=fcompany, 
            roll=froll, 
            eligibility=feligibility, 
            email= femail,
            address=faddress, 
            phonenumber=fphonenumber
        )


n= int(input("Enter how many number of records u want to create: "))
# hyd_populate(n)
# print(f"{n} records created successfully......")

# pune_populate(n)
# print(f"{n} records created successfully......")

banglore_populate(n)
print(f"{n} records created successfully......")