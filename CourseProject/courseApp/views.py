from django.shortcuts import render
import datetime

# Create your views here.
def courseinfo(request):
    date= datetime.datetime.now()
    name= "Django"
    prerequisite= "Python"
    sname1= "Ajit"
    sname2= "Amiya"
    sname3= "Soumya"
    rollno1= 101
    rollno2= 102
    rollno3= 103
    mark1= 83
    mark2=84
    mark3=86

    my_dict= {"date":date, "name":name, "prerequisite":prerequisite}

    return render(request, "courseApp/index.html", context=my_dict)