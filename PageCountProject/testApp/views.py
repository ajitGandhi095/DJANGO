from django.shortcuts import render

# Create your views here.

def cookies_view(request):
    print("Cookies from the client: ", request.COOKIES)
    count= int(request.COOKIES.get('count', 0))
    count= count+1
    my_dict= {'count':count}
    response= render(request,'testApp/index.html', my_dict)
    response.set_cookie('count', count)
    return response