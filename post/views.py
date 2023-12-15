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
from django.utils import timezone


# def test_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Test view')


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! It`s my project')


def current_date_view(request):
    current_date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current date and time: {current_date}")

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")


