from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', max_length=250, verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']