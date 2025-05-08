from django import forms

class Signupform(forms.Form):
    email= forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        print("Validate all Fields")
        total_data= super().clean()

        #Email Field
        print("Email Validate")
        inputemail= total_data['email']
        if inputemail[-10:] != "@gmail.com":
            raise forms.ValidationError("Email must be @gmail.com")
        
        #Password field
        print("Password Validate")
        inputpwd= total_data['password']
        if len(inputpwd) < 8 :
            raise forms.ValidationError("Password must be 8 char onwords")\
        
        #Repassword field
        print("Repassword field")
        inputpwd1= total_data['password']
        inputpwd2= total_data['repassword']
        if inputpwd1 != inputpwd2:
            raise forms.ValidationError("Password didn't match")