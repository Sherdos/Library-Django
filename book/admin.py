from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title', )}

admin.site.register(Books)
admin.site.register(Category, CategoryAdmin)


