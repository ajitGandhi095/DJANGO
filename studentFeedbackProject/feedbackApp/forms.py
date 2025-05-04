from django import forms

class studDetails(forms.Form):
    name= forms.CharField()
    rollno= forms.IntegerField()
    email= forms.EmailField()
    address= forms.CharField(widget=forms.Textarea)