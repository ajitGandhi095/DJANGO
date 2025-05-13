from django.shortcuts import render
from django.views.generic import ListView
from testApp.models import Book

# Create your views here.

class BookListView(ListView):
    model= Book
