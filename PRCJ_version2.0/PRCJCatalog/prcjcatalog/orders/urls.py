from django.urls import path, include
from orders import views

urlpatterns = [
    path('', views.practice),
    path("order-item/", views.listOrderItemView.as_view()),
    path("order-item/<int:pk>", views.modifyOrderItemView.as_view()),
    path("list/", views.listOrdersView.as_view()),
    path("list/<int:pk>", views.modifyOrderView.as_view()),
]