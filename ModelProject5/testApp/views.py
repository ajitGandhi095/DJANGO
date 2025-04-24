from django.shortcuts import render
from testApp.models import Employee
# Create your views here.
def empl_data(request):
    emp= Employee.objects.all()
    my_dict={"data": emp}
    return render(request, 'testApp/index.html', my_dict)