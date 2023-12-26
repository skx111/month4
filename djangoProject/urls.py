"""
urls.py - Файл маршрутизации Django-проекта.

admin.site.urls - URL-адреса административного сайта.

path - функция для создания маршрута.
Принимает 2 аргумента:
1) Путь (строка)
2) Обработчик (функция, которая будет обрабатывать запрос)
"""
from django.contrib import admin
from django.urls import path

from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.product_list_view),
    path('hello/', views.hello_view),
    path('date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('categories/', views.category_list_view),


]
