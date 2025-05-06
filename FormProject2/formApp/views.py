from django.shortcuts import render
from formApp.form import EmployeeForm

# Create your views here.

def empView(request):
    submit= False
    ename= ''
    form= EmployeeForm()
    if request.method == "POST":
        form= EmployeeForm(request.POST)
        if form.is_valid():
            print("Form Submitted Successfully")
            print("*"*30)
            print("EName: ", form.cleaned_data['ename'])
            print("Email: ", form.cleaned_data['email'])
            print("Edsg: ", form.cleaned_data['edsg'])
            print("Esal: ", form.cleaned_data['esal'])
            print("Esec: ", form.cleaned_data['esec'])
            print("*"*30)
            submit=True
            ename= form.cleaned_data['ename']
        else:
            print("Validate name field failed")

    my_dict= {'form':form, 'submit':submit, 'ename':ename}

    return render(request, 'formApp/index.html', my_dict)