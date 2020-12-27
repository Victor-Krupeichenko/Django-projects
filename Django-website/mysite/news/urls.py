# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', name='category'),
    # path('news/<int:news_id>/', name='view_news'),
    # path('news/add-news/', name='add_news')
#
]