from apps.book.models import Category


menu = [
        {'title': "Главная", 'url_name': 'index'},
        {'title': "О сайте", 'url_name': 'about'},
    ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['cats']=cats
        context['menu']=menu
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context