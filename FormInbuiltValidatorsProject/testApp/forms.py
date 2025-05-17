from django import forms
from django.core import validators

def feedback_valid(value):
        print("Feedback Validation")
        if len(value) < 10:
            raise forms.ValidationError("Feedback between be 10 to 100 chars")
def gmail_valid(value):
     print("Gmail Validation")
     if value[-10:] != "@gmail.com":
          raise forms.ValidationError("Email Should be @gmail.com")
        
class StudentForm(forms.Form):
    name= forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    rollno= forms.IntegerField()
    email= forms.EmailField(validators=[gmail_valid])
    feedback= forms.CharField(widget=forms.Textarea, validators=[feedback_valid])