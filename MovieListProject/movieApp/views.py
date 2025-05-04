from django.shortcuts import render
from movieApp.models import MovieModel
from movieApp.forms import MovieForm

# Create your views here.

def mainView(request):
    return render(request, 'movieApp/index.html')

def listView(request):
    movie_list= MovieModel.objects.all()
    msg= "All The Movie List"
    my_dict= {'movie_list':movie_list, 'msg':msg}
    return render(request, 'movieApp/movieList.html', my_dict)

def addView(request):
    submitted= False
    mname= ''
    if request.method == 'POST':
        form= MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Movie added in DB successfully.....")
            print("*"*30)
            print("Movie Name: ", form.cleaned_data['title'])
            print("Hero: ", form.cleaned_data['hero'])
            print("Heroine: ", form. cleaned_data['heroine'])
            print('Release: ', form.cleaned_data['release'])
            print("*"*40)
            submitted= True
            mname= form.cleaned_data['title']
    form= MovieForm()
    my_dict= {'form':form, 'submit':submitted, 'mname':mname}
    return render(request, 'movieApp/movieAdd.html', my_dict)