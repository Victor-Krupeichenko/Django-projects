from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Текст')
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('title', 'category')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    ordering = ('-created_at',)
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75"')
        else:
            return 'Нет фото'

    get_photo.short_description = 'Миниатюра'
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Упровление новостями'
admin.site.site_header = 'Управление новостями'
