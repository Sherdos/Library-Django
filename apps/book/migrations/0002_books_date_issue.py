# Generated by Django 4.1.5 on 2023-02-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='date_issue',
            field=models.DateField(null=True, verbose_name='Дата выпуска'),
        ),
    ]
