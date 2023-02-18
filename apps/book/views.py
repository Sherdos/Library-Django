from django.shortcuts import render
from django.views.generic import ListView, DetailView
import fitz
from .models import *
# Create your views here.

class IndexView(ListView):
    model = Books
    template_name = 'book/index.html'
    context_object_name = 'books'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


class BookCategoryView(ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['books'][0].category)
        context['cat_selected'] = context['books'][0].category_id
        return context
    
    def get_queryset(self):
        return Books.objects.filter(category__slug=self.kwargs['cat_slug'])


class ShowBookView(DetailView):
    model = Books
    template_name = 'book/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['book']
        context['cat_selected'] = context['book'].category_id
        return context


class SearchBookView(ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        key = self.request.GET.get('key')
        return Books.objects.filter(title__icontains = key)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        context['cat_selected'] = 0
        return context





# class BookReadView(DetailView):
#     template_name = 'book/detail.html'
#     context_object_name = 'book'
#     model = Books
    

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Читать'
#         book = fitz.open('media/'+str(context['book'].book))
#         context['page'] = self.get(self.request.GET)
#         return context

#     def get(self, request, **kwargs):
#         book = fitz.open('media/'+str(self.model.book))
#         if request.GET == 'page':
#             page = book.load_page(int(self.request.GET.get('page')))
#             return page.get_text("text")

#     def get_queryset(self):
#         return Books.objects.get(slug=self.kwargs['slug'])
    
        







def about(request):
    context = {
        'title':'О сайте',
    }
    return render(request, 'book/index.html', context)



def book_read(request, slug):
    book = Books.objects.get(slug=slug)
    book_url = fitz.open('media/'+str(book.book))
    try:
        page_number = int(request.GET.get('page'))
        page = book_url.load_page(page_number)
    except:
        page_number = 1
        page = book_url.load_page(0)
    lase_page = book_url.page_count
    page_text = page.get_text("html")
    context = {
        'page':page_text,
        'page_number':page_number,
        'lase_page':lase_page,
        'book_url':book_url
    }
    return render(request, 'book/detail.html', context)




