from django.shortcuts import render

# Create your views here.
def staticfiles(request):
    return render(request, 'testApp/index.html')