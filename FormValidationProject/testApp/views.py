from django.shortcuts import render
from testApp.form import FormValidation

# Create your views here.

def validation_view(request):
    submit=False
    name=''
    form= FormValidation()

    if request.method == "POST":
        form= FormValidation(request.POST)
        if form.is_valid():
            print("Form Submitted Successfully....")
            print("*"*30)
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("*"*30)
            submit=True
            name= form.cleaned_data['name']

    my_dict= {'form':form, 'submit':submit, 'name':name}

    return render(request, 'testApp/index.html', my_dict)