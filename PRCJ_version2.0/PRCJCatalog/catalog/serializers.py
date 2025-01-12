from rest_framework import serializers
from users.models import Users, Products, Price, GoldPrice, Category, Orders, OrderDetails

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
