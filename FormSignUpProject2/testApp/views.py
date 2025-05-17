from django.shortcuts import render
from testApp.forms import UserForm

# Create your views here.

def userView(request):
    submit=False
    uname=''
    form= UserForm()

    if request.method == "POST":
        form= UserForm(request.POST)
        if form.is_valid():
            print("Form Submitted")
            print("*"*30)
            print("First Name: ", form.cleaned_data['firstname'])
            print("Last Name: ", form.cleaned_data['lastname'])
            print("Email: ", form.cleaned_data['email'])
            print("Password: ", form.cleaned_data['pwd'] )
            print("RePassword: ", form.cleaned_data['repwd'])
            print("*"*30)
            submit=True
            uname= form.cleaned_data['firstname']

    my_dict = {'form':form, 'submit':submit, 'uname':uname}
    return render(request, 'testApp/index.html', my_dict)