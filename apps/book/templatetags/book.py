from django import template 
from apps.book.models import *

register = template.Library() 
 
# @register.simple_tag(name='getcat')
# def get_categories():
#     return Category.objects.all()


@register.inclusion_tag('book/include/sidebar.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats':cats, 'cat_selected':cat_selected}


@register.inclusion_tag('book/include/header.html')
def navbar():
    menu = [{'title': "Главная", 'url_name': 'index'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Админ панель", 'url_name':'admin:index'}
    ]
    return {'menu':menu}



@register.inclusion_tag('book/include/paginator.html')
def paginator_num(book_url, request=None):
    lase_page = book_url.page_count
    try:
        page_number = int(request.GET.get('page'))
    except:
        page_number = 1
    page_next = page_number + 1
    page_previous = page_number - 1
    context = {
        'page_next':page_next,
        'page_previous':page_previous,
        'lase_page':lase_page,
        'page_number':page_number
    }
    return context


