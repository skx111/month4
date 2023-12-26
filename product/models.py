'''
models.py - Файл моделей приложения.
'''

from django.db import models

# class Product(models.Model):
#     photo = models.ImageField(upload_to='products', null=True, blank=True)
#     name = models.CharField(max_length=150)
#     description = models.TextField()
#     price = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
#
#     class Meta:
#         abstract = True
#
# class Category(BaseModel):
#     name = models.CharField(max_length=255, verbose_name='Название')
#
#     def __str__(self) -> str:
#         return f'{self.name}'
#
#     class Meta:
#         db_table = 'category'
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#
# class Product(BaseModel):
#     image = models.ImageField(
#         upload_to='products',
#         null=True,
#         blank=False,
#         verbose_name='Фото'
#         )
#     title = models.CharField(max_length=255, verbose_name='Заголовок')
#     text = models.TextField(null=True, blank=True, verbose_name='Текст')
#     rate = models.FloatField(default=0, verbose_name='Рейтинг')
#     category = models.ManyToManyField(
#
#     )


from django.db import models

# class Product(models.Model):
#     title = models.CharField(max_length=255, default='Default Title')

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True


class Hashtag(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = 'hashtag'
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


class Product(BaseModel):
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=False,
        verbose_name="Фото"
        )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(null=True, blank=True, verbose_name="Текст")
    rate = models.FloatField(default=0, verbose_name="Рейтинг")
    hashtags = models.ManyToManyField(
        Hashtag,
        verbose_name="Хэштеги",
        related_name="products"
    )

    def __str__(self) -> str:
        return f"{self.title} {self.rate}"

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(BaseModel):
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="categories"
    )
    text = models.TextField(null=True, blank=True, verbose_name="Текст")

    def __str__(self) -> str:
        return f"{self.text}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


