'''
admin.py - Файл настроек административного сайта.
'''


from django.contrib import admin
from product.models import Product, Hashtag, Category



# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'created_at', 'updated_at']
#     list_display_links = ['id', 'title']
#     search_fields = ['title', 'text']
#     list_filter = ['created_at']
#     ordering = ['created_at']

admin.site.register(Product)
admin.site.register(Hashtag)
admin.site.register(Category)


