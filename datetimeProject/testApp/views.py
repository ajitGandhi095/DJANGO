from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def datetime_info(request):
    date= datetime.datetime.now()
    h= int(date.strftime("%H"))

    msg= '<h1> Hello Friends '
    if h<12:
        msg += "Good Morning"
    elif h<16:
        msg += "Good Afternoon"
    elif h<21:
        msg += "Good Evening"
    else :
        msg += "Good Night"
    msg += "</h1> <hr>"

    msg += "Now the server time is: " + str(date)

    return HttpResponse(msg)