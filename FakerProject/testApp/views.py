from django.shortcuts import render
from testApp.models import STUDENT
# Create your views here.

def studinfo(request):
    # stud_list = STUDENT.objects.all()
    # stud_list = STUDENT.objects.filter(marks__gt=50)
    # stud_list = STUDENT.objects.filter(marks__lt=50)
    # stud_list = STUDENT.objects.filter(name__startswith='S')
    # stud_list = STUDENT.objects.order_by('marks')
    stud_list = STUDENT.objects.order_by('-marks')
    my_dict= {"stud_list":stud_list}
    return render(request, 'testApp/index.html', my_dict)