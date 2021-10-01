from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    slug = models.SlugField(max_length=255, verbose_name='urls', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ['title']

class Product(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название продукта')
    is_published = models.BooleanField(default = True, verbose_name='Опубликовать?')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Опубликовано')
    count = models.IntegerField(default=0, verbose_name='Количество товара')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']

class Img(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='img')
    img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Изображение продкута'
        verbose_name_plural = 'Изображении продуктов'
        ordering = ['product']