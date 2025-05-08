from django import forms
from django.core import validators

def start_with_s(value):
    print("Name First Char Validate")
    if value[0].lower() != 's':
        raise forms.ValidationError("Name Should be start with s or S")
def gmail_valid(value):
     print("@gmail.com Validation")
     if value[-10:] != "@gmail.com":
         raise forms.ValidationError("Gmail must be @gmail.com")
        
class StudentForm(forms.Form):
    name= forms.CharField(validators=[start_with_s])
    rollno= forms.IntegerField()
    email= forms.EmailField(validators=[gmail_valid])
    feedback= forms.CharField(widget=forms.Textarea, validators=[validators.MinLengthValidator(10), validators.MaxLengthValidator(100)])
    

    