"""
urls.py - Файл маршрутизации Django-проекта.

admin.site.urls - URL-адреса административного сайта.

path - функция для создания маршрута.
Принимает 2 аргумента:
1) Путь (строка)
2) Обработчик (функция, которая будет обрабатывать запрос)
"""
from django.contrib import admin
from django.urls import path, include

from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/', views.product_list_view),
    path('hello/', views.hello_view),
    path('date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('categories/', views.category_list_view),
    path('product/create/', views.product_create_list_view),
    path('product/<int:product_id>/', views.product_detail_view),
    path('product/create/', views.product_create_view),
    path('category/create/', views.category_create_view),
    path('', include('product.urls')),
    path('auth/', include('user.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)