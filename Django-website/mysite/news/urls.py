# -*- coding: utf-8 -*-
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('user-logout', user_logout, name='user_logout'),
    path('user-login', user_login, name='user_login'),
    path('user-register', user_register, name='user_register'),
    path('',cache_page(60) (NewsHome.as_view()), name='home'),
    path('category/<int:category_id>/', NewsCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('send-mail/', user_contact_mail, name='user_contact_mail'),
]