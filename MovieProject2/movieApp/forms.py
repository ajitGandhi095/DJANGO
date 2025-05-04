from django import forms
from movieApp.models import MovieModel
class MovieForm(forms.ModelForm):
    class Meta:
        model= MovieModel
        fields= '__all__'