from django import forms

class StudentForm(forms.Form):
    name= forms.CharField(max_length=40)
    marks= forms.FloatField()