from django.shortcuts import render
import datetime

# Create your views here.

def employee(request):
    date= datetime.datetime.now()
    msg= "Hello!! guest very good "
    h= int(date.strftime("%H"))
    if(h<12):
        msg += "morning"
    elif(h<16):
        msg += "afternoon"
    elif(h<20):
        msg += "evening"
    else:
        msg += "night"
    my_dict= {"date":date, "msg":msg}
    return render(request, "employeeInfo/index.html", context=my_dict)