from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products, Price, GoldPrice, Category
from products.serializers import ProductSerializer, PriceSerializer, GoldPriceSerializer, CategorySerializer
from rest_framework import generics, permissions, status

# Create your views here.
def practice(request):
    print("Products Test")
    prods = Price.objects.all()
    for i in prods:
        print(i.get_product_price)
    return HttpResponse(request)

# Product View - list
class listProductsView(generics.ListCreateAPIView):
    # goldprice = 192.23
    # Products.objects.update(price = F('price')*goldprice)
    # print(Products.objects.all())
    # print("select ", Products.objects.select_related('category').all())
    # print("prefetch_related ", Products.objects.prefetch_related('category').all())
    queryset = Products.objects.all() #prefetch_related('price').all()
    serializer_class = ProductSerializer

class updateProductsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all() #prefetch_related('price').all()
    serializer_class = ProductSerializer

# Products with prices view
class listPriceView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class updatePriceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

# Gold Price (Should be an API call to get LIVE price)
class createGoldPriceView(generics.ListCreateAPIView):
    queryset = GoldPrice.objects.all()
    serializer_class = GoldPriceSerializer

class updateGoldPriceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoldPrice.objects.all()
    serializer_class = GoldPriceSerializer

# Category View - list
class listCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class updateCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
