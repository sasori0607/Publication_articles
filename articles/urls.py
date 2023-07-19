from django.urls import path
from .views import (
    create_article,
    article_list,
    article_delete
)

urlpatterns = [
    path('', article_list, name='article_list'),
    path('create/', create_article, name='create_article'),
    path('articles/<int:pk>/delete/', article_delete, name='article_delete'),
]
