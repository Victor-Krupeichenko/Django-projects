from .forms import NewsForm
from .models import News, Category
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class NewsHome(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsHome, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'item'

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super(CreateNews, self).get_context_data(**kwargs)
        context['title'] = 'Добавить новость'
        return context