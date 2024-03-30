from typing import Any
from django.http import FileResponse, HttpRequest, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.core.cache import cache
from apps.book.models import Book
from apps.book.utils import DataMixin, photo_page

# ListView
class IndexView(DataMixin, ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='Главная'))
        return context
    
    def get_queryset(self):
        if 'books' not in cache:
            cache.set('books', Book.objects.all().order_by('-id'), 60)
        return cache.get('books')

# DetailView
class ShowBookView(DataMixin, DetailView):
    queryset = Book.objects.all()
    template_name = 'book/show/show_book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title=context['book'].title))
        return context
    
    

# Read online
class BookReadView(DataMixin, View):
    template_name = 'book/show/read.html'
    
    def get(self, request, *args: Any, **kwargs: Any):
        try:
            book = Book.objects.get(slug=kwargs['book_slug'])
            page = int(request.GET.get('page', 1))
            photo = photo_page(book, page)
            context = {
                'photo': photo,
                'page_next': page + 1,
                'page_previous': max(1, page - 1),
                'page': page
            }
            context.update(self.get_user_context())
            return render(request, self.template_name, context)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
    
    