from django import forms
from testApp.models import companyModel

class companyForm(forms.ModelForm):
    name= forms.CharField()
    location= forms.CharField()
    ceo= forms.CharField()
    bot_handler= forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model= companyModel
        fields= '__all__'

    def clean(self):
        print("Total Data Validation")
        total_data= super().clean()

        print("Name Validation")
        inputname= total_data['name']
        if len(inputname) < 10:
            raise forms.ValidationError("Company name must be 10 chars onwords")
        
        print("Location Validation")
        inputlocation= total_data['location']
        if len(inputlocation) < 8:
            raise forms.ValidationError("Location must be 8 chars onwords")
        
        print("Ceo Validation")
        inputceo= total_data['ceo']
        if len(inputceo) < 10:
            raise forms.ValidationError("Ceo Name must be 10 chars onwords")
        
        print("Bot Validation")
        inputbot= total_data['bot_handler']
        if len(inputbot) > 0:
            raise forms.ValidationError("We don't accept bot request")