from django import forms

class FormValidation(forms.Form):
    name= forms.CharField()
    rollno= forms.IntegerField()
    email= forms.EmailField()
    message= forms.CharField(widget=forms.Textarea)

    # Validate Field
    def clean(self):
        print("Total foem field Validating")
        total_data= super().clean()

        #Name Validation
        print("Name Validation")
        inputname= total_data['name']
        if len(inputname) < 4 :
            raise forms.ValidationError("Name must be 4 char onwords and not digit")
        
        #rollno Validation
        print("Rollno Validation")
        inputroll= total_data['rollno']
        if inputroll <= 0:
            raise forms.ValidationError("Rollno is greater then zero rollno > 0")
        
        #Email Validation
        print("Email Validation")
        inputmail= total_data['email']
        if inputmail[-10:] != "@gmail.com":
            raise forms.ValidationError("Email must be @gmail.com")
        
        #Message Validation
        print("Message Validation")
        inputmsg= total_data['message']
        if (len(inputmsg) < 10 and len(inputmsg) > 100) :
            raise forms.ValidationError("Message must be 10 to 100 character")