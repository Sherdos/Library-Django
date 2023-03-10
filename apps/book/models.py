from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название')
    slug = models.SlugField(verbose_name='Человекопонятный URL (само генерация)', max_length=255, unique=True, db_index=True)
    book = models.FileField(verbose_name='Книга', upload_to='book/')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='автор', null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='book_image/')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE,related_name='category_book')
    create = models.DateTimeField(auto_now_add=True,verbose_name='Дата добавление',)
    date_issue = models.DateField(verbose_name='Дата выпуска',null=True)
    buyer = models.ManyToManyField(User, verbose_name='покупатели')
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['date_issue']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show_book", kwargs={"book_slug": self.slug})
    
    
class Category(models.Model):
    title = models.CharField( max_length=255, verbose_name='Название')
    slug = models.SlugField(verbose_name='Человекопонятный URL (само генерация)', max_length=255, unique=True, db_index=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_book_index", kwargs={"cat_slug": self.slug})


class Author(models.Model):
    name = models.CharField(max_length=70,verbose_name='Имя')
    slug = models.SlugField(verbose_name='Человекопонятный URL (само генерация)', max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='image_author/', verbose_name='Фото Автора', null=True, blank=True, default='no_image.png')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("show_author", kwargs={"slug": self.slug})
    
    


    

