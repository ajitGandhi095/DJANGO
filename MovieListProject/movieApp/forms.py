from django import forms
from movieApp.models import MovieModel

class MovieForm(forms.ModelForm):
    title= forms.CharField()
    hero= forms.CharField()
    heroine= forms.CharField()
    release= forms.DateField()

    class Meta:
        model= MovieModel
        fields= '__all__'