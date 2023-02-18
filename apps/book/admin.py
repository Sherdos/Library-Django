from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug' : ('title', )}
    search_fields = ('title','id')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'date_issue')
    list_display_links = ('title','id')
    list_filter = ('category','create','date_issue')
    list_editable = ('category',)
    prepopulated_fields = {'slug' : ('title', )}
    search_fields = ('title',)



admin.site.register(Books, BookAdmin)

admin.site.register(Category, CategoryAdmin)


