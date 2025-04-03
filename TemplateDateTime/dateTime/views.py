from django.shortcuts import render
import datetime

# Create your views here.
def servertime(request):
    date= datetime.datetime.now()
    my_dict= {"date":date}
    return render(request, 'dateTime/index.html', context={"date":date})