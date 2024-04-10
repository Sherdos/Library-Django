import json
from django.contrib.auth.models import User
from django.core.cache import cache
from django.views.generic import ListView, DetailView
from apps.book.models import Book, Category
from apps.book.tasks import delete_photos
from apps.book.utils import DataMixin
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, IntervalSchedule



class BookCategoryView(DataMixin, ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            category = Category.objects.get(slug=self.kwargs['cat_slug'])
            category_name = category.title
            c_def = self.get_user_context(title=f'Категория - {category_name}')
            context.update(c_def)
        except Category.DoesNotExist:
            # Handle the case where the category does not exist
            pass
        return context
    
    def get_queryset(self):
        categories_slug = self.kwargs.get('cat_slug')
        cached_books = cache.get('books_' + categories_slug)
        if not cached_books:
            cached_books = Book.objects.filter(categories__slug=categories_slug)
            cache.set('books_' + categories_slug, cached_books, 60)
        return cached_books
    
class SearchBookView(DataMixin, ListView):
    template_name = 'book/index.html'
    context_object_name = 'books'
    paginate_by = 6

    def get_queryset(self):
        key = self.request.GET.get('key')
        if key:
            return Book.objects.filter(title__icontains=key)
        return Book.objects.none()  # Return an empty queryset if no key is provided

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поиск')
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


def test(request):
    delete_photos()
    return HttpResponse('HEllo')

def test2(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every = 30,
        period = IntervalSchedule.SECONDS
    )
    
    PeriodicTask.objects.create(
        interval = interval,
        name = 'My-schedule',
        task = 'apps.book.task.delete_photos',
        # args = json.dump(['Arg1','Arg2'])
        # one_off = True
    )
    return HttpResponse('Task') 