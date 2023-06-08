from django import template 
from apps.book.models import *

register = template.Library()

@register.inclusion_tag('book/components/pag.html')
def paginator_num(book_url, request):
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


