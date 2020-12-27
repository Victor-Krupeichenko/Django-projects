from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsForm
from .models import News, Category
from django.views.generic import ListView, CreateView

class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'