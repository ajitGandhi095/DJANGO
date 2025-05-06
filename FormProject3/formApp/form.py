from django import forms

class EmployeeForm(forms.Form):
    ename= forms.CharField(label="Employee Name")
    email= forms.EmailField(label="Email")
    edsg= forms.CharField(label="Designation")
    esal= forms.FloatField(label="Salery")
    esec= forms.CharField(label="Section")

    def clean_ename(self):
        print("Validate Name Field")
        inputname= self.cleaned_data['ename']
        if len(inputname) < 3:
            raise forms.ValidationError("Employee name min 3 char onwords and not only digit")
        return inputname