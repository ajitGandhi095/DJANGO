from django.shortcuts import render
from testApp.models import Teacher

# Create your views here.
def teacher_data(request):
    teacher_list= Teacher.objects.all()
    my_dict= {'teacher':teacher_list}

    return render(request, 'testApp/index.html', my_dict)