from django.shortcuts import render
from django.http import HttpResponse
from news.models import News


def index(request):
    news = News.odjects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)