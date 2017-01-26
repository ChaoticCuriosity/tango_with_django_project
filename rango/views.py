from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    #return render(request, '/rango/index.html/', context=context_dict)
    Html = "Rango says hey there partner! <a href='/rango/about/'>About</a><br />"
    return HttpResponse(Html)


def about(request):

    Html = "Rango says welcome to the about page! <a href='/rango/'>Index</a><br />"
    return HttpResponse(Html)


