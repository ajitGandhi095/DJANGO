from django.shortcuts import render
from readformApp.form import StudForm

# Create your views here.

def studData(request):
    submit=False
    sname=''
    if request.method == 'POST':
        form= StudForm(request.POST)
        if form.is_valid():
            print("Form Validation Successfull and Print Data")
            print("*"*20)
            print("Name: ", form.cleaned_data['name'])
            print("Rollno: ", form.cleaned_data["rollno"])
            print("Marks: ", form.cleaned_data["marks"])
            print("*"*20)
            sname=form.cleaned_data['name']
            submit=True
    form= StudForm()
    my_dict= {"form":form, 'submit':submit, 'sname':sname}
    return render(request, 'readformApp/index.html', my_dict)

