'''
views.py - Файл представлений приложения.
View - это функция, которая принимает запрос и возвращает ответ.

HttpResponse - класс, который представляет собой ответ сервера.

HTTP - протокол передачи гипертекста. HyperText Transfer Protocol.
HTTPs - защищенный протокол передачи гипертекста. HyperText Transfer Protocol Secure.

Method - метод. GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD.

render - функция, которая принимает запрос, имя шаблона и словарь с данными и возвращает ответ.
'''


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from product.models import Product, Category, Review
from django.utils import timezone
from product.forms import ProductForm, ProductForm2, CategoryCreateForm, ReviewCreateForm



def main_view(request):
    if request.method == 'GET':
        return render(request, 'product/ index.html')


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


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, '404.html')

        context = {
            'product': product,
        }
        return render(
            request,
            'product/detail.html',
            context=context
        )


# def hello_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Hello! It`s my project')

#
# def current_date_view(request):
#     current_date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
#     return HttpResponse(f"Current date and time: {current_date}")
#
# def goodbye_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Goodbye user!")


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


def product_create_view(requests):
    if requests.method == 'GET':
        context = {
            'form': ProductForm2,
        }
        return render(requests, 'product/create.html', context=context)

    if requests.method == 'POST':
        form = ProductForm2(requests.POST, requests.FILES)

        if form.is_valid():
            form.save()

            return redirect('/products/')
        else:
            context = {
                'form': form,
            }

            return render(requests, 'product/create.html', context=context)

def category_create_view(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/categories/')
    else:
        form = CategoryCreateForm()
    return render(request, 'categories/create.html', {'form': form})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = request.user
            new_review.save()
            return redirect('/product_detail/', product_id=product.id)
    else:
        form = ReviewCreateForm()

    return render(request, 'product/detail.html', {'product': product, 'reviews': reviews, 'form': form})




