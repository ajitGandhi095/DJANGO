from django.shortcuts import render
from testApp.form import Signupform

# Create your views here.

def signup_view(request):
    submit=False
    form= Signupform()
  
    if request.method == "POST":
        form= Signupform(request.POST)
        if form.is_valid():
            print("*"*30)
            print("Signup Successfully")
            print("Email: ", form.cleaned_data['email'])
            print("*"*30)
            submit=True
            
    my_dict= {'form':form, 'submit':submit}
    return render(request, 'testApp/index.html', my_dict)
