from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def exam_view(req):
    return HttpResponse("<h1>Exam View</h1>")

def attendance_view(req):
    return HttpResponse("<h1>Attendance View</h1>")

def fees_view(req):
    return HttpResponse("<h1>Fees View</h1>")