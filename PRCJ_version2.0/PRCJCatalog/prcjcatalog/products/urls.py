from django.urls import path
from products import views

urlpatterns = [

    path("", views.practice),
    path("category/", views.listCategoryView.as_view()),
    path("category/<int:pk>", views.updateCategoryView.as_view()),
    path("gold-price/", views.createGoldPriceView.as_view()),
    path("gold-price/<int:pk>", views.updateGoldPriceView.as_view()),
    path("details/", views.listProductsView.as_view()),
    path("details/<int:pk>", views.updateProductsView.as_view()),
    path("with-prices/", views.listPriceView.as_view()),
    path("with-prices/<int:pk>", views.updatePriceView.as_view()),
]