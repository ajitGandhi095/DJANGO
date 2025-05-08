from django.shortcuts import render
from testApp.form import StudentForm

# Create your views here.

def student_view(request):
    submit=False
    sname=''
    form= StudentForm()

    if request.method == "POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            print("Form Submitted Successfully....")
            print("*"*30)
            print("Name: ", form.cleaned_data['name'])
            print("Rollno: ", form.cleaned_data['rollno'])
            print("Email: ", form.cleaned_data['email'])
            print("*"*30)
            submit=True
            sname= form.cleaned_data['name']

    my_dict= {"form":form, "submit":submit, "sname":sname}

    return render(request, 'testApp/index.html', my_dict)
