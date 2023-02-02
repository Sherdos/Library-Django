from django.db import models

# Create your models here.


class Setting(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название сайта'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    logo = models.FileField(
        upload_to='logo/',
        verbose_name='логотип сайта',
        validators=[]
    )