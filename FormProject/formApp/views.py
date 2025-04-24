from django.shortcuts import render
from formApp.form import StudentForm

# Create your views here.

def stud_data(request):
    list= StudentForm()
    my_dict= {"list":list}

    return render(request, 'formApp/index.html', my_dict)