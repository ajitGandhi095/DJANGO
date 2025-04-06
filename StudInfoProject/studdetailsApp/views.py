from django.shortcuts import render
import datetime
# Create your views here.
def studdetails(request):
    time = datetime.datetime.now()
    cname= "Django"
    prerequisite= "Python"

    my_dict= {"time":time, "cname":cname, "prerequisite":prerequisite}
    return render(request, "studdetailsApp/index.html", my_dict)