from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('book/read/<slug:slug>/', book_read, name='read_book'),
    path('book/<slug:book_slug>/', ShowBookView.as_view(), name='show_book'),
    path('category/<slug:cat_slug>/', BookCategoryView.as_view(), name='category_book_index'),
    path('serch/', SearchBookView.as_view(), name='search_book'),
]
