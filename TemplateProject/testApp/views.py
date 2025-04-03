from django.shortcuts import render

# Create your views here.
def template(req):
    return render(req, 'testApp/index.html')