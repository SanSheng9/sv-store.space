from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='urls', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название продукта')
    is_published = models.BooleanField(default = True, verbose_name='Опубликовать?')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']