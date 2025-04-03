from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyd_job_info(request):
    s="Details about Hyderabad jobs"
    return HttpResponse(s)

def ban_job_info(request):
    s="Details about Bengalore jobs"
    return HttpResponse(s)

def pune_job_info(request):
    s="Details Pune about jobs"
    return HttpResponse(s)

def kol_job_info(request):
    s="Details about Kolkata jobs"
    return HttpResponse(s)