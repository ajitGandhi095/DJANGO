from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authApp.form import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.

def home_view(request):
    return render(request, 'authApp/home.html')

@login_required
def java_view(request):
    return render(request, 'authApp/javaexam.html')

@login_required
def python_view(request):
    return render(request, 'authApp/pythonexam.html')

@login_required
def aptitude_view(request):
    return render(request, 'authApp/aptitudeexam.html')

def signup_view(request):
    submit= False
    uname= ''
    form= SignUpForm()

    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            user.set_password(user.password)
            user.save()
            print("Form Submitted")
            return HttpResponseRedirect('/accounts/login')

    my_dict= {"form":form, "submit":submit, "uname":uname}
    return render(request, 'authApp/signup.html', my_dict)

def logout_view(request):
    return render(request, 'authApp/logout.html')
