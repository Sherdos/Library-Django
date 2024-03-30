from django.http import FileResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
import fitz
from apps.book.models import Book, Category
from django.core.cache import cache
from django.db.models import Count
import os

MENU_ITEMS = [
    {'title': "Главная", 'url_name': 'index'},
    {'title': "О сайте", 'url_name': 'about'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('categories')
        if not cats:
            cats = Category.objects.annotate(count=Count('book'))
            cache.set('categories', cats, 60)
        context['cats'] = cats
        context['menu'] = MENU_ITEMS
        return context

def photo_page(book: Book, page_number: int) -> str:
    book_path = os.path.join('media', str(book.book))
    try:
        with fitz.open(book_path) as book_file:
            if page_number < 0 or page_number >= len(book_file):
                raise ValueError("Page number is out of range")
            page = book_file.load_page(page_number)
            mat = fitz.Matrix(300 / 72, 300 / 72)
            pix = page.get_pixmap(matrix=mat)
            photo = f"media/photo/{book.slug}_page{page_number}.png"
            pix.save(photo)
            return photo
    except Exception as e:
        print(f"Error generating photo: {e}")
        return ""
    
def add_favorite(request: HttpRequest, book_slug):
        try:
            book = Book.objects.get(slug=book_slug) 
            book.favorites.add(request.user)
        except Book.DoesNotExist:
            return redirect('book:index')
        return redirect('book:show_book', book_slug)
    
def download(request: HttpRequest, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    try:
        return FileResponse(book.book.open(), as_attachment=True)
    except Book.DoesNotExist:
        return redirect('book:show_book', book_slug)
        