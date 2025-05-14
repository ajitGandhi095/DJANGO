from django.shortcuts import render
from django.views.generic import ListView
from testApp.models import Book

# Create your views here.

class BookListView(ListView):
    model= Book

class BookListView2(ListView):
    model= Book
    template_name= 'testApp/books.html'
    context_object_name= 'books'
