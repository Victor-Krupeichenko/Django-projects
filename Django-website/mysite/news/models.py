from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    content = models.TextField(db_index=True, verbose_name='содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'updated_at', 'title']

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
