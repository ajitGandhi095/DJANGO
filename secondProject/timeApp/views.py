from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def time_info(request):
    date= datetime.datetime.now()
    res=""" 
       <h1> Hello friends good evening!!!!! </h1>
       <hr><br>
    """
    res= res + "Now Server Time Is: "+ str(date)

    return HttpResponse(res)