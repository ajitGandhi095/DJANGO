from django.shortcuts import render
from testApp.models import Employee

# Create your views here.

def employeeView(request):
    emp_list= Employee.objects.all()
    return render(request, 'testApp/index.html', {'emp_list':emp_list})