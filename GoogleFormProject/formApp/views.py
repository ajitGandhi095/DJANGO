from django.shortcuts import render
from formApp.form import StudentFeedback
import datetime

# Create your views here.

def feedbackView(request):
    date= datetime.datetime.now()
    today_date= date.strftime('%d-%m-%Y')
    submit= False
    sname=''
    form= StudentFeedback()

    if request.method == "POST":
        form= StudentFeedback(request.POST)
        if form.is_valid():
            print("Student Feedback Form Submitted Successfully...")
            print("*"*30)
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Course: ", form.cleaned_data['course'])
            print("*"*30)
            submit=True
            sname= form.cleaned_data['name']
    my_dict= {'form':form, 'submit':submit, 'sname':sname, 'date':today_date}

    return render(request, 'formApp/index.html', my_dict)