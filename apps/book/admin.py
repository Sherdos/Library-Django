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


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image')
    list_display_links = ('name','id')
    list_filter = ('name',)
    list_editable = ('image',)
    prepopulated_fields = {'slug' : ('name', )}
    search_fields = ('name',)



admin.site.register(Books, BookAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Author, AuthorAdmin)


