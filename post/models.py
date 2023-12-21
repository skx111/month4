'''
models.py - Файл моделей приложения.
'''

from django.db import models

class Product(models.Model):
    photo = models.ImageField(upload_to='products', null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


