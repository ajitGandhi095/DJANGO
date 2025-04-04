from django.shortcuts import render
import datetime
# Create your views here.

def dateTime(request):
    date= datetime.datetime.now()
    name= "Ajit"
    rollno= 101
    marks= 87
    my_dict={"date":date, "name":name, "rollno":rollno, "marks":marks}
    return render(request, "datetimeApp/index.html", context=my_dict)