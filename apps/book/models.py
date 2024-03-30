from django.urls import reverse
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from transliterate import translit

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    book = models.FileField(upload_to='books/', verbose_name='Файл книги')
    description = models.TextField(verbose_name='Описание')
    authors = models.ManyToManyField('Author', verbose_name='Авторы')
    image = models.ImageField(upload_to='book_images/', verbose_name='Фото')
    categories = models.ManyToManyField('Category', verbose_name='Категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    date_of_issue = models.DateField(verbose_name='Дата выпуска книги', null=True)
    favorites = models.ManyToManyField(User, verbose_name='В избранном', blank=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('date_of_issue',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.title,'ru', reversed=True))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book:show_book", kwargs={"book_slug": self.slug})

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.title,'ru', reversed=True))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book:category_book_index", kwargs={"cat_slug": self.slug})

class Author(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    image = models.ImageField(upload_to='author_images/', verbose_name='Фото автора', null=True, blank=True, default='no_image.png')
    biography = models.TextField(verbose_name='Биография', blank=True, null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.title,'ru', reversed=True))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book:show_author", kwargs={"slug": self.slug})
