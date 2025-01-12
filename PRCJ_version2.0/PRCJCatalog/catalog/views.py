from django.shortcuts import render
from users.models import Users, Products, Price, GoldPrice, Category, Orders, OrderDetails
from users.serializers import AccountSerializer, ProductSerializer, PriceSerializer, GoldPriceSerializer, CategorySerializer, OrderSerializer, OrderItemSerialzier
from rest_framework import generics, permissions, status
from django.db.models import F # Used to updating a column value by adding, multiplying, dividing.. a scalar to it 

# If issues occur when migrating then use "python manage.py migrate --fake", it fakes the migration
# def save(self, *args, **kwargs) method in models to update a column value right at database level
# CharField - choices; imageField - upload_to; DateTimeField - auto_now_add; DecimaField - max-digits; 

# User View - create, retrieve, update, destroy
class createUserView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = AccountSerializer

class modifyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = AccountSerializer




