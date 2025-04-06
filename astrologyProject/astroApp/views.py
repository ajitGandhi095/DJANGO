from django.shortcuts import render
import datetime, random
# Create your views here.

def astro(request):
    time = datetime.datetime.now()
    h= int(time.strftime("%H"))
    msg= ""

    if h<12:
        msg += "Good Morning"
    elif h<16:
        msg += "Good Afternoon"
    elif h<21:
        msg += "Good Evening"
    else:
        msg += "Good Night"

    msg_list= [
        "The golden days ahead",
        "Better to sleep more time even in classroom",
        "Tommorrow will be the best day of your life",
        "Tommorrow is the best day to purpose your gf",
        "Very soon you will get job"
    ]

    name_list= ["Deepika", "Katrina", "Alia", "Tara", "Jackline"]
    goodmsg= random.choice(msg_list)
    name= random.choice(name_list)

    my_dict= {"wish":msg, "time":time, "msg":goodmsg, "name":name}

    return render(request, "astroApp/index.html", my_dict)
