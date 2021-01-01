from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at','is_published', 'get_photo')
    list_display_links = ('title', 'category')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    ordering = ('-created_at', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75"')
        else:
            return 'Нет фото'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title', )
    search_fields = ('title', )

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Упровление новостями'
admin.site.site_header = 'Управление новостями'


