from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('book/<int:id>/', book_read, name='book_read'),
    path('<str:slug>/', category_index, name='category_index'),
]
