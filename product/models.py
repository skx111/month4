'''
models.py - Файл моделей приложения.
'''


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



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


class Review(models.Model):
    product = models.ForeignKey('product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.rating}'


