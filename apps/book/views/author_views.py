from django.views.generic import DetailView
from apps.book.models import Author
from apps.book.utils import DataMixin

class ShowAuthor(DataMixin, DetailView):
    model = Author
    template_name = 'book/show/show_author.html'
    context_object_name = 'author'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_name = context['author'].name
        title = f'Автор - {author_name}'
        context.update(self.get_user_context(title=title))
        return context
