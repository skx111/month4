'''
views.py - Файл представлений приложения.
View - это функция, которая принимает запрос и возвращает ответ.

HttpResponse - класс, который представляет собой ответ сервера.

HTTP - протокол передачи гипертекста. HyperText Transfer Protocol.
HTTPs - защищенный протокол передачи гипертекста. HyperText Transfer Protocol Secure.

Method - метод. GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD.

render - функция, которая принимает запрос, имя шаблона и словарь с данными и возвращает ответ.
'''


from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Category
from django.utils import timezone



def main_view(request):
    if request.method == 'GET':
        return render(request, 'product/index.html')

# def main_view(request):
#     return render(request, 'layouts/main.html')

# def products_view(request):
#     products = Product.objects.all()
#     return render(request, 'products/main.html', {'products': products})


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! It`s my project')


def current_date_view(request):
    current_date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current date and time: {current_date}")

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")


def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products,
        }
        return render(
            request,
            'product/products.html',
            context=context
        )
def category_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            'categories': categories,
        }
        return render(
            request,
            'product/categories.html',
            context=context
        )







