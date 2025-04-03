from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s= "<h1>Hello Ajit!! Welcome to Django. Hope your journey is great and enjoyful.</h1>"
    return HttpResponse(s)