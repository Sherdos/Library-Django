from django.shortcuts import render

from apps.book.models import *
from apps.setting.imports import All
from apps.setting.logick import icon_url

# Create your views here.

def index(request):
    all = All()
    books = Books.objects.all()
    category = Category.objects.all()
    urls =  icon_url(category)
    context = {
        'books':books,
        'category':category,
        'all':all,
        'urls':urls
    }
    return render(request, 'index.html', context)