from django.shortcuts import render
from movieApp.models import MovieModel
from movieApp.forms import MovieForm

# Create your views here.

def main_view(request):
    return render(request, 'movieApp/index.html')

def list_view(request):
    movie_list= MovieModel.objects.all()

    return render(request, 'movieApp/list.html', {'movie_list':movie_list})

def add_view(request):
    submit= False
    mname=''
    form= MovieForm()
    if request.method == "POST":
        form= MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Movie Added into DB Successfully")
            print("Movie Title: ", form.cleaned_data['title'])
            print("Hero: ", form.cleaned_data['hero'])
            print("Heroine: ", form.cleaned_data['heroine'])
            print("Release Date: ", form.cleaned_data['release'])
            submit=True
            mname=form.cleaned_data['title']
            # return main_view(request)
        
    my_dict= {'form':form, 'submit':submit, 'mname':mname}
    return render(request, 'movieApp/add.html', my_dict)