from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug' : ('title', )}
    search_fields = ('title','id')
    
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'date_issue', 'get_html_photo')
    list_display_links = ('title','id')
    list_filter = ('category','create','date_issue')
    list_editable = ('category',)
    prepopulated_fields = {'slug' : ('title', )}
    search_fields = ('title',)
    fields = ('title','slug','get_html_photo','category','description','book','author','image','date_issue','create')
    readonly_fields = ('date_issue','create','get_html_photo')

    def get_html_photo(self,object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        
    get_html_photo.short_description = 'Фото'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'get_html_photo')
    list_display_links = ('name','id')
    list_filter = ('name',)
    prepopulated_fields = {'slug' : ('name', )}
    search_fields = ('name',)
    fields = ('name','slug','description','get_html_photo','image')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self,object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
        
    get_html_photo.short_description = 'Фото'


admin.site.register(Books, BookAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Author, AuthorAdmin)

admin.site.site_title='Lib'
admin.site.site_header='Lib'

