# -*- coding: utf-8 -*-
from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('category/<int:category_id>/', NewsCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]