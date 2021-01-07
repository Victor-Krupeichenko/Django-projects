from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse_lazy

class News(models.Model):
    title = models.CharField(db_index=True, max_length=150, verbose_name='Название')
    content = RichTextUploadingField(db_index=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at']

    def get_absolute_url(self):
        context = {
            'pk': self.pk
        }
        return reverse_lazy('view_news', kwargs=context)



class Category(models.Model):
    title = models.CharField(db_index=True, max_length=150, verbose_name='Категория')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def get_absolute_url(self):
        context ={
            'category_id': self.pk
        }
        return reverse_lazy('category', kwargs=context)

