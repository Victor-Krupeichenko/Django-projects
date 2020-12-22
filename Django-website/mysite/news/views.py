from django.shortcuts import render
from .models import News, Category

def index(request):
    news = News.objects.all()
    context = {
        'news':news,
        'title':'Список новостей',
    }
    return render(request, 'news/index.html', context)

def get_categories(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news':news,
        'category': category
    }
    return render(request, 'news/category.html', context)

def view_news(request, news_id):
    item = News.objects.get(pk=news_id)
    context = {
        'item':item
    }
    return render(request, 'news/view_news.html', context)