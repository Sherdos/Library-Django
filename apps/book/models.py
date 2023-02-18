from django.urls import reverse
from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(
        max_length=255,    
        verbose_name='Название'
    )
    slug = models.SlugField(
        verbose_name='Человекопонятный URL (само генерация)',
        max_length=255,
        unique=True,
        db_index=True
    )
    book = models.FileField(
        verbose_name='Книга',
        upload_to='book/'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='book_image/'
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        on_delete=models.CASCADE,
        related_name='category_book'
    )
    create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление',
    )
    date_issue = models.DateField(
        verbose_name='Дата выпуска',
        null=True
    )
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def get_absolute_url(self):
        return reverse("show_book", kwargs={"book_slug": self.slug})

    def __str__(self):
        return self.title

    
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    slug = models.SlugField(
        verbose_name='Человекопонятный URL (само генерация)',
        max_length=255,
        unique=True,
        db_index=True
    )
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category_book_index", kwargs={"cat_slug": self.slug})




    

