from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsForm
from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)


def get_categories(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    item = get_object_or_404(News, pk=news_id)
    context = {
        'item': item
    }
    return render(request, 'news/view_news.html', context)


def add_news(request):
    if request.method =='POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    context = {
        'form': form
    }
    return render(request, 'news/add_news.html', context)
