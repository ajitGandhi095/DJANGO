from django.shortcuts import render
from testApp.forms import StudentForm

# Create your views here.

def studentView(request):
    submit= False
    sname= ''
    form= StudentForm()

    if request.method == "POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            print("form Submitted")
            print("*"*30)
            print("Name: ", form.cleaned_data['name'])
            print("RollNo: ", form.cleaned_data['rollno'])
            print("Email: ", form.cleaned_data['email'])
            print("*"*30)
            submit= True
            sname= form.cleaned_data['name']

    my_dict = {'form':form, 'submit':submit, 'sname':sname}
    return render(request, 'testApp/index.html', my_dict)