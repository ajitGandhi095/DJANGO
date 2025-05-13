from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

# Create your views here.

class TemplateCBV(TemplateView):
    template_name= 'testApp/results.html'

class TemplateContext(TemplateView):
    template_name= 'testApp/results2.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['date']= datetime.datetime.now()
        context['name']= "Ajit"
        context['subject']= "Django"
        context['marks']= 67.89

        return context