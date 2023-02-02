from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from .logick import create_book
# Create your views here.
def category_index(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    context= {
        'category':category,
        'categories':categories
    }
    return render(request, 'category_index.html', context)

def book_read(request, id):
    page = create_book(id)
    paginator = Paginator(page, 1)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    context = {
        'pages':pages,
        'page':page
    }
    return render(request, 'detail.html', context)