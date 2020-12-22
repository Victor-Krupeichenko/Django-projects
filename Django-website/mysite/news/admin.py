from django.contrib import admin

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('title', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    search_fields = ('title',)


class NewsCategory(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('category',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, NewsCategory)