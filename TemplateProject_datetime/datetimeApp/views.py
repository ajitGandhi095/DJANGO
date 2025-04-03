from django.shortcuts import render
import datetime

# Create your views here.
def time(request):
    date= datetime.datetime.now()
    # my_dict= {'insert_date':date}
    # return render(request, 'datetimeApp/index.html',my_dict)
    # OR
    return render(request, 'datetimeApp/index.html', {'insert_date':date})
