from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    #path('<str:param>', views.index),
    path('', views.search_redirect),
    path('<int:id>', views.BookView.as_view(), name='show_book'),
]