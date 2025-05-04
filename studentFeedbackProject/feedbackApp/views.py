from django.shortcuts import render
from feedbackApp.forms import studDetails

# Create your views here.

def studView(request):
    submit=False
    sname=''

    if request.method == "POST":
        form= studDetails(request.POST)
        if form.is_valid():
            print("Form Validation Successfull and print feedback Information")
            print("*"*30)
            print("Name: ", form.cleaned_data['name'])
            print("Rollno: ", form.cleaned_data['rollno'])
            print("Email: ", form.cleaned_data['email'])
            print("Address: ", form.cleaned_data['address'])
            submit= True
            sname= form.cleaned_data['name']
    form= studDetails()
    my_dict= {'form':form, 'submit':submit, 'sname':sname}
    return render(request, 'feedbackApp/index.html', my_dict)