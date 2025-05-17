from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from testApp.models import companyModel
from testApp.forms import companyForm
from django.urls import reverse_lazy
# Create your views here.

class companyListView(ListView):
    model= companyModel
    template_name= 'testApp/companyList.html'
    context_object_name= 'company_list'

class companyDetailView(DetailView):
    model= companyModel
    template_name= 'testApp/company_details.html'
    context_object_name= 'company'

class companyCreateView(CreateView):
    model= companyModel
    form_class = companyForm
    template_name= 'testApp/company_create.html'
    context_object_name= 'form'

class companyUpdateView(UpdateView):
    model= companyModel
    form_class = companyForm
    template_name= 'testApp/company_update.html'
    context_object_name= 'company'

class companyDeleteView(DeleteView):
    model= companyModel
    success_url= reverse_lazy('list')
    template_name= 'testApp/company_delete.html'
    context_object_name= 'company'
    
