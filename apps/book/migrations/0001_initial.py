# Generated by Django 4.1.5 on 2023-02-12 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Человекопонятный URL (само генерация)')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Человекопонятный URL (само генерация)')),
                ('book', models.FileField(upload_to='book/', verbose_name='Книга')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='book_image/', verbose_name='Фото')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_book', to='book.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
