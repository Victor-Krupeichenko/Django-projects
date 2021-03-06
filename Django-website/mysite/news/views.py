from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .models import News, Category, UserContactMail
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from django.core.mail import EmailMessage, get_connection
from django.db.models import F


def user_contact_mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            con = get_connection()
            con.open()
            mail = EmailMessage(form.cleaned_data['subject'], form.cleaned_data['content'],
                            'Victor_krupeichenko@hotmail.com', ['krupeichenkovictor@gmail.com'], connection=con)
            if request.FILES:
                file = request.FILES['files']
                mail.attach(file.name, file.read(), file.content_type)
                mail.send(fail_silently=True)
                con.close()
                messages.success(request, 'Письмо успешно отправлено!')
                return redirect('home')
            if mail:
                mail.send(fail_silently=True)
                con.close()
                messages.success(request, 'Письмо успешно отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки!')
        else:
            messages.error(request, 'Ошибка валидации!!!')
    else:
        form = ContactForm()
    return render(request, 'news/user_mail.html', {'form':form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации!!!')
    else:
        form = UserRegisterForm()
    return render(request, 'news/user_register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/user_login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('user_login')



class NewsHome(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

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
    paginate_by = 2

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

    def get_context_data(self, **kwargs):
        context = super(ViewNews, self).get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super(CreateNews, self).get_context_data(**kwargs)
        context['title'] = 'Добавить новость'
        return context


class SendEmail(CreateView):
    form_class = UserContactMail
    template_name = 'news/user_register.html'