from apps.book.models import Category
from django.core.cache import cache
from django.db.models import Count



class DataMixin:
    
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(count=Count('category_book'))
            cache.set('cats', cats, 60*4)
        context['cats']=cats
        context['menu']=self.menu()
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context
    
    
    
    def menu(self):
        menu = {'right':[
            {'title': "Выйти", 'url_name': 'logout'},
            {'title': "Войти", 'url_name': 'login'},
            {'title': "Регистрация", 'url_name': 'register'}
            ],
        'left':[
            {'title': "Главная", 'url_name': 'index'},
            {'title': "Админ панель", 'url_name': 'admin:index'},
            ]
        }
        if not self.request.user.is_authenticated:
            right=menu['right']
            del right[0]
        else:
            right=menu['right']
            del right[1:3]
            
        if not self.request.user.is_superuser:
            left=menu['left']
            del left[1]  
        return menu