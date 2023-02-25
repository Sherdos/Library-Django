from django.urls import path
from .views import *


urlpatterns = [
                # url                          # view                   # name
    # book
    path('',                            IndexView.as_view(),          name='index'),
    path('book/<slug:book_slug>/',      ShowBookView.as_view(),       name='show_book'),
    path('category/<slug:cat_slug>/',   BookCategoryView.as_view(),   name='category_book_index'),
    path('serch/',                      SearchBookView.as_view(),     name='search_book'),
    
    # auth
    path('login/',                      LoginUserView.as_view(),      name='login'),
    path('register/',                   RegisterUserView.as_view(),   name='register'),
    path('logout/',                     logout_user,                  name='logout'),
    
    # other
    path('about/',                      about,                        name='about'),
    path('book/<int:id>/<str:str>/',          dow,                          name='dow'),
]
