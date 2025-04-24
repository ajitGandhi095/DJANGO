from django.shortcuts import render
from jobApp.models import HYD, PUNE, BANGALORE

# Create your views here.

def main_page(request):
    return render(request, 'jobApp/index.html')

def hydjob(request):
    hyd_list= HYD.objects.all().order_by('company')
    msg= "Hyderabad Jobs Information"
    type="hyd"
    my_dict= {'hyd_list':hyd_list, 'msg':msg, 'type':type}
    return render(request, 'jobApp/details.html', my_dict)

def punejob(request):
    pune_list= PUNE.objects.all().order_by('company')
    msg= 'Pune Jobs Information'
    type= "pune"
    my_dict= {'pune_list':pune_list, 'msg':msg, 'type':type}
    return render(request, 'jobApp/details.html', my_dict)

def bangjobs(request):
    bang_list= BANGALORE.objects.all()
    msg= 'Banglore Jobs Information'
    type= "bang"
    my_dict= {'bang_list':bang_list, 'msg':msg, 'type':type}
    return render(request, 'jobApp/details.html', my_dict)