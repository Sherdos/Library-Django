from django.urls import path
from apps.book.utils import add_favorite, download
from apps.book.views.author_views import ShowAuthor
from apps.book.views.book_views import BookReadView, IndexView, ShowBookView
from apps.book.views.other_views import BookCategoryView, MyBookView, SearchBookView

app_name = 'book'  # Optional namespace for the app

urlpatterns = [
    # Book
    path('', IndexView.as_view(), name='index'),
    path('book/<slug:book_slug>/', ShowBookView.as_view(), name='show_book'),
    path('book/read/<slug:book_slug>/', BookReadView.as_view(), name='read'),
    path("book/favorite/<slug:book_slug>/", add_favorite, name="add_favorite"),
    path("book/download/<slug:book_slug>/", download, name="download"),
    
    # Other
    path('category/<slug:cat_slug>/', BookCategoryView.as_view(), name='category_book_index'),
    path('search/', SearchBookView.as_view(), name='search_book'),
    path("my_book/<int:pk>/", MyBookView.as_view(), name="my_book"),
    
    
    # Author
    path('author/<slug:slug>/', ShowAuthor.as_view(), name='show_author'),
]