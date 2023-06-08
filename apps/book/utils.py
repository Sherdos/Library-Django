from apps.book.models import Category
from django.core.cache import cache
from django.db.models import Count

menu = [
        {'title': "Главная", 'url_name': 'index'},
        {'title': "О сайте", 'url_name': 'about'},
    ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(count=Count('category_book'))
            cache.set('cats', cats, 60)
        context['cats']=cats
        context['menu']=menu
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context