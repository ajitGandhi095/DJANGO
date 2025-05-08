from django import forms
from django.core import validators
        
class StudentForm(forms.Form):
    name= forms.CharField()
    rollno= forms.IntegerField()
    email= forms.EmailField()
    feedback= forms.CharField(widget=forms.Textarea)

    # Validation all the fields
    def clean(self):
        print("Validate All the fields")
        total_data= super().clean()

        # Name Validation
        print("Name Validation")
        inputname= total_data['name']
        if (inputname[0].lower() != 's' and len(inputname) <4):
            raise forms.ValidationError("Name must be 4 char onwords and start with s or S")
        
        # Rollno Validation
        print("Rollno Validation")
        inputroll= total_data['rollno']
        if inputroll <= 0 :
            raise forms.ValidationError("Rollno is greater then 0 rollno > 0")
        
        # Email Validation
        print("Email Validation")
        inputgmail= total_data['email']
        if inputgmail[-10:] != "@gmail.com":
            raise forms.ValidationError("email should be @gmail.com")
        
        # Feedback Validation
        print("Feedback Validation")
        inputmsg= total_data['feedback']
        if (len(inputmsg) < 10 and len(inputmsg) > 100):
            raise forms.ValidationError("Message must be 10 to 100 character")
    

    