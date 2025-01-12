from rest_framework import serializers
from users.models import Users

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
