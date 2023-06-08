import os
from typing import Any
from django import http
from django.db.models.query import QuerySet
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
        c_def = self.get_user_context(title='Главная',description = 'Новинки')
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
        c_def = self.get_user_context(
            title='Категория - ' + str(context['cat']),
            cat_selected=context['books'][0].category_id,
            description = f'Книги по категории {context["cat"]}'
        )
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
        c_def = self.get_user_context(title='Поиск',description='Все найденные книги по вашему запросу')
        context.update(c_def)
        return context

class MyBookView(DataMixin, ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return self.request.user.books_set.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Мои книги',description='Мои книги')
        context.update(c_def)
        return context
    
# DetailView

class ShowBookView(DataMixin, DetailView):
    queryset = Books.objects.all()
    template_name = 'book/show/book/show.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['book'], cat_selected=context['book'].category_id)
        context.update(c_def)
        return context
    
    def post(self, request, *args, **kwargs):
        book = Books.objects.get(id=request.POST.get('book_id')) 
        return FileResponse(book.book.open(), as_attachment=True)
    
    
    
class ShowAuthor(DataMixin, DetailView):
    model = Author
    template_name = 'book/show/author/show.html'
    context_object_name = 'author'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Автор - '+str(context['author'].name))
        context.update(c_def)
        return context
    
    

    
    

class BookReadView(DataMixin,View):
    template_name = 'book/show/book/read.html'
    
    def get(self, request, *args: Any, **kwargs: Any):
        book = Books.objects.get(id=kwargs['pk'])
        page=request.GET.get('page')
        page_url=request.GET.get('page_url')
        
        if page is None:
            page=1
        con_dop = self.photo_page(book,int(page),request)
        self.photo_page_delete(page_url)
        page_next = int(page) + 1
        page_previous = int(page) - 1
        context = {
            'page_next':page_next,
            'page_previous':page_previous,
            'page':page
        }
        context.update(con_dop)
        return render(request, self.template_name, context)
  
    def photo_page(self, book,page_number,request):
        book_url = fitz.open('media/'+str(book.book))
        count = book_url.page_count
        page = book_url.load_page(page_number)
        mat = fitz.Matrix(300/72, 300/72)
        pix = page.get_pixmap(matrix=mat)
        photo = f"media/photo/{book.slug} page{page_number}-{request.user.username}.png"
        pix.save(photo)
        context = {
            'count_page':count,
            'photo':photo
        }
        return context

    def photo_page_delete(self,photo):
        if photo is not None:
            if os.path.exists(photo):
                os.remove(photo)





def logout_user(request):
    logout(request)
    return redirect('index')
        


    







