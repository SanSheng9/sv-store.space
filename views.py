from django.shortcuts import render
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from shop.models import Product, Img, Category
from shop.serializers import ProductsSerializer, ImgsSerializer, CategoriesSerializer


def ProductsList(request):
   return render(request, 'shop/index.html')

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_published']

class ImgViewSet(ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = ImgsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['product']

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['parent']