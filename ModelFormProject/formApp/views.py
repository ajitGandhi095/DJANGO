from django.shortcuts import render
from formApp.forms import StudentForm

# Create your views here.

def studentView(request):
    submitted= False
    sname= ''
    if request.method == "POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Record Inserted into DB Successfully.....")
            print("*"*30)
            print("name: ", form.cleaned_data['name'])
            print("Rollno: ", form.cleaned_data['rollno'])
            print("Marks: ", form.cleaned_data['marks'])
            print("*"*30)
            submitted= True
            sname= form.cleaned_data['name']
    form= StudentForm()
    my_dict= {'form':form, 'submit':submitted, 'name':sname}

    return render(request, 'formApp/index.html', my_dict)
