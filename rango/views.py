from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages'; page_list}
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context_dict)
    #Html = "Rango says hey there partner! <a href='/rango/about/'>About</a><br />"
    #return HttpResponse(Html)


def about(request):
    about_context_dict = {'boldmessage': "About: This is a page about things; REAL things!"}
    return render(request, 'rango/about.html', context=about_context_dict)

    #Html = "Rango says welcome to the about page! <a href='/rango/'>Index</a><br />"
    #return HttpResponse(Html)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict[ 'pages' ] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)



