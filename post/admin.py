'''
admin.py - Файл настроек административного сайта.
'''


from django.contrib import admin

from post.models import Product

admin.site.register(Product)


