from django.shortcuts import render
from formApp.form import StudentForm

# Create your views here.

def student_view(request):
    submit=False
    name=''
    form= StudentForm()

    if request.method == "POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            print("Form submitted successfully")
            print("*"*30)
            print("Name: ", form.cleaned_data['name'])
            print("Rollno: ", form.cleaned_data['rollno'])
            print("*"*30)
            submit=True
            name= form.cleaned_data['name']
    my_dict= {'form':form, 'submit':submit, 'name':name}
    return render(request, 'formApp/index.html', my_dict)
            