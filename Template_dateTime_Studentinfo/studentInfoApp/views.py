from django.shortcuts import render
import datetime

# Create your views here.
def studentinfo(request):
    date= datetime.datetime.now()
    name= "Ajit"
    marks= 83
    roll= 101

    my_dict= {"date":date, "name":name, "marks":marks, "roll":roll}
    return render(request, "studentInfoApp/index.html", context=my_dict)
