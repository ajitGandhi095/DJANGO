from django.shortcuts import render
from testApp.models import Teacher
# Create your views here.

def readTeacher(request):
    list_teacher= Teacher.objects.all()
    my_dict= {'teacher':list_teacher}

    return render(request, 'testApp/index.html', my_dict)