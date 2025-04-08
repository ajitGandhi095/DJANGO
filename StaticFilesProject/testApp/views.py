from django.shortcuts import render

# Create your views here.

def staticfiles(request):
    subjects = {'s1':"Python", 's2':"Django", 's3':"RESTAPI"}
    return render(request, 'testApp/index.html', subjects)