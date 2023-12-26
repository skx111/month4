'''
admin.py - Файл настроек административного сайта.
'''


from django.contrib import admin
from product.models import Product, Hashtag, Category

admin.site.register(Product)
admin.site.register(Hashtag)
admin.site.register(Category)


