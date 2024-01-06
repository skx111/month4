from django.urls import path

from product import views


urlpatterns = [
    path('', views.main_view),
    path('products/', views.product_list_view),
    path('products/create/', views.product_create_view),
    path('products/<int:product_id>/', views.product_detail_view),
    path('categories/', views.category_list_view),
]