from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Orders, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerialzier
from rest_framework import generics, permissions, status


# Create your views here.

# How to use _set, select_related, prefetch_related

def practice(request):
    print("Orders Test")
    orders = Orders.objects.all()
    for i in orders:
        print(i.pk, i.get_cart_total, i.no_of_items_in_cart)
    print('-------')
    for i in OrderItem.objects.all():
        print(i.order.pk, i.product.product.name, i.get_total_per_quantity)
    return HttpResponse({'values': orders})

# Order View - Create, retrieve, update, Destroy
class listOrdersView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class modifyOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

# OrderItem View - create, retrieve, update, destroy
class listOrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerialzier

class modifyOrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerialzier
