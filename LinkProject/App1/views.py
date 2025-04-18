from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "App1/index.html")

def login(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/login.html', my_dict)

def signup(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/signup.html', my_dict)

def about(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/navbar.html', my_dict)

def offers(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/navbar.html', my_dict)

def news(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/navbar.html', my_dict)

def contact(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/navbar.html', my_dict)