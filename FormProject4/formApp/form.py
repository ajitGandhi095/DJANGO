from django import forms

class StudentForm(forms.Form):
    name= forms.CharField(
        label="Student Name" ,
        widget=forms.TextInput(attrs={"placeholder": "Enter Full Name"})
    )
    rollno= forms.CharField(
        label="Rollno" ,
        widget=forms.TextInput(attrs={"placeholder": "Enter RollNo"})
    )

    def clean_name(self):
        print("Validate Name Field")
        inputname= self.cleaned_data['name']
        if len(inputname) < 8:
            raise forms.ValidationError("Name minimum 8 characters")
        return inputname