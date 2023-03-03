from django.http import FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from .utils import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.core.cache import cache
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
    
    
    
    
class ShowAuthor(DataMixin, DetailView):
    model = Author
    template_name = 'book/show/show_author.html'
    context_object_name = 'author'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Автор - '+str(context['author'].name))
        context.update(c_def)
        return context
    
    


# CreateView

class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'book/auth.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description']='Пожалуйста, заполните эту форму, чтобы создать учетную запись.'
        c_def = self.get_user_context(title='Регистрация')
        context.update(c_def)
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
        
        
           
class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'book/auth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description']='Пожалуйста, заполните эту форму, чтобы войти в учетную запись.'
        c_def = self.get_user_context(title='Авторизация')
        context.update(c_def)
        return context
    
    def get_success_url(self):
        return reverse_lazy('index')

    





def dow(request,id,str):
    if 'dow' in str:
        book = Books.objects.get(id=id)
        return FileResponse(book.book.open(), as_attachment=True)
    elif 'read' in str:
        book = Books.objects.get(id=id)
        return FileResponse(book.book.open(), content_type='application/pdf')
  

  
def about(request):
    context = {
        'title':'О сайте',
    }
    return render(request, 'book/index.html', context)



def logout_user(request):
    logout(request)
    return redirect('index')

