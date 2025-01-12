from django.contrib import admin
from catalog.models import Users, Category, Products, Orders, OrderDetails

# Register your models here.

admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderDetails)