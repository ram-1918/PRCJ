from rest_framework import serializers
from orders.models import Orders, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderItemSerialzier(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'