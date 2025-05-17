from django import forms

class UserForm(forms.Form):
    firstname= forms.CharField()
    lastname= forms.CharField()
    email= forms.EmailField()
    pwd= forms.CharField(widget=forms.PasswordInput)
    repwd= forms.CharField(widget=forms.PasswordInput)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        print("Total Data")
        total_data= super().clean()

        print("FirstName Validation")
        inputfname= total_data['firstname']
        if len(inputfname) < 4:
            raise forms.ValidationError("Firstname must be 4 chars onwords")
        
        print("LastName Validation")
        inputlname= total_data['lastname']
        if len(inputlname) < 3:
            raise forms.ValidationError("LastName Must be 3 chars onwords")
        
        print("Email Validation")
        inputemail= total_data['email']
        if inputemail[-10:] != "@gmail.com":
            raise forms.ValidationError("Email Extension is '@gmail.com'")
        
        print("pwd Validation")
        inputpwd= total_data['pwd']
        if len(inputpwd) < 8 :
            raise forms.ValidationError("Password must be 8 chars onwords")
        
        print("Repwd validation")
        inputrepwd= total_data['repwd']
        inputpwd = total_data['pwd']
        if inputrepwd != inputpwd :
            raise forms.ValidationError("Confirm Password didn't match.. try again")
        
        print("Bot handle")
        inputbot= total_data['bot_handler']
        if len(inputbot) > 0:
            raise forms.ValidationError("We don't accept bot Request")
