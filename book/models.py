from django.db import models



# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    slug = models.SlugField(
        verbose_name='Слаг'
    )
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Books(models.Model):
    title = models.CharField(
        max_length=255,    
        verbose_name='Название'
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
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        related_name='category_book'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


    

