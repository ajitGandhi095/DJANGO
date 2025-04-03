from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_view(req):
    return HttpResponse("<h1>First View Response</h1>")

def second_view(req):
    return HttpResponse("<h1>Second View Response</h1>")

def third_view(req):
    return HttpResponse("<h1>Third View Response</h1>")