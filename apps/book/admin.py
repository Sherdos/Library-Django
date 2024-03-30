from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Book, Author

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_of_issue', 'get_html_photo')
    list_display_links = ('title', 'id')
    list_filter = ('categories', 'created_at', 'date_of_issue')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'get_html_photo', 'favorites')
    fieldsets = (
        (None, {'fields': ('title', 'categories', 'description', 'book', 'authors', 'image')}),
        ('Date Information', {'fields': ('date_of_issue',), 'classes': ('collapse',)}),
        ('Read-only Fields', {'fields': ('created_at', 'get_html_photo', 'favorites'), 'classes': ('collapse',)})
    )

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = 'Фото'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo')
    list_display_links = ('name', 'id')
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = 'Фото'

admin.site.site_title = 'LibMed Админ'
admin.site.site_header = 'LibMed Администрация'
