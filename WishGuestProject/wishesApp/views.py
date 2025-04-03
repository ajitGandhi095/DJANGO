from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date= datetime.datetime.now()
    msg= "Hello!! Guest "
    h= int(date.strftime('%H'))

    if h<12:
        msg+="Very Good Morning"
    elif h<16:
        msg+="Very Good Afternoon"
    elif h<20:
        msg+="Very Good Evening"
    else:
        msg+="Very Good Night"

    name= "Ajit"
    rollno= 101
    marks=83

    my_dict= {"date":date, "msg":msg, "name":name, "rollno":rollno, "marks":marks}
    return render(request, "wishesApp/index.html", context=my_dict)