from django.shortcuts import render
from users.models import Users
from users.serializers import AccountSerializer
from rest_framework import generics, permissions, status
from django.db.models import F # Used to updating a column value by adding, multiplying, dividing.. a scalar to it 


# User View - create, retrieve, update, destroy
class createUserView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = AccountSerializer

class modifyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = AccountSerializer




