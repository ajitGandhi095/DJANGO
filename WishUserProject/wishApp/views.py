from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    date= datetime.datetime.now()
    h= int(date.strftime("%H"))
    msg= "Hello!! Guest Very "

    if h<12:
        msg += "Good Morning"

    elif h<16:
        msg += "Good Afternoon"

    elif h<21:
        msg += "Good Evening"
    else:
        msg += "Good Night"

    my_dict= {"date":date, "msg":msg}

    return render(request, "wishApp/index.html", my_dict)