from django import forms
from formApp.models import StudentModel

class StudentForm(forms.ModelForm):
    name= forms.CharField()
    rollno= forms.IntegerField()
    marks= forms.FloatField()

    class Meta:
        model= StudentModel
        fields= "__all__"