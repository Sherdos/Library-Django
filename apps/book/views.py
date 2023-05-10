from typing import Any
from django import http
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,View
from .models import *
from .forms import *
from .utils import *
from django.core.cache import cache
import fitz
from django.contrib.auth import logout
# Create your views here.

# ListView

class IndexView(DataMixin, ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная')
        context.update(c_def)
        return context
    
    def get_queryset(self):
        cach = cache.get('books')
        if not cach:
            cach = Books.objects.all().order_by('-id')
            cache.set('books', cach, 60)
        return cach



class BookCategoryView(DataMixin,ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = context['books'][0].category
        c_def = self.get_user_context(title='Категория - ' + str(context['cat']), cat_selected=context['books'][0].category_id)
        context.update(c_def)
        return context
    
    def get_queryset(self):
        cach = cache.get('books'+str(self.kwargs['cat_slug']))
        if not cach:
            cach = Books.objects.filter(category__slug=self.kwargs['cat_slug'])
            cache.set('books'+str(self.kwargs['cat_slug']), cach, 60)
        return cach



    

class SearchBookView(DataMixin, ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        key = self.request.GET.get('key')
        return Books.objects.filter(title__icontains = key)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поиск')
        context.update(c_def)
        return context



# DetailView

class ShowBookView(DataMixin, DetailView):
    queryset = Books.objects.all()
    template_name = 'book/show/show_book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['book'], cat_selected=context['book'].category_id)
        context.update(c_def)
        return context
    
    def post(self, request, *args, **kwargs):
        book = Books.objects.get(id=request.POST.get('book_id')) 
        if 'buy' in request.POST:
            book.buyer.add(request.user)
        elif 'read' in request.POST:
            return FileResponse(book.book.open())
        return redirect('show_book', book.slug )
            
    
    
    
class ShowAuthor(DataMixin, DetailView):
    model = Author
    template_name = 'book/show/show_author.html'
    context_object_name = 'author'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Автор - '+str(context['author'].name))
        context.update(c_def)
        return context
    
    
class MyBookView(DataMixin, DetailView):
    model = User
    template_name = 'book/my_book.html'
    content_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мои книги')
        context.update(c_def)
        return context
    
    

class BookReadView(DataMixin,View):
    template_name = 'book/show/read.html'
    
    def get(self, request, *args: Any, **kwargs: Any):
        book = Books.objects.get(id=kwargs['pk'])
        page=request.GET.get('page')
        if page is None:
            page=1
        photo = self.photo_page(book,int(page))
        page_next = int(page) + 1
        page_previous = int(page) - 1
        context = {
            'photo':photo,
            'page_next':page_next,
            'page_previous':page_previous,
            'page':page
        }
        return render(request, self.template_name, context)
  
    def photo_page(self, book,page_number):
        book_url = fitz.open('media/'+str(book.book))
        page = book_url.load_page(page_number)
        mat = fitz.Matrix(300/72, 300/72)
        pix = page.get_pixmap(matrix=mat)
        photo = f"media/photo/{book.slug} page{page_number}.png"
        pix.save(photo)
        return photo




def logout_user(request):
    logout(request)
    return redirect('index')
        


    







