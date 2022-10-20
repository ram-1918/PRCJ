from django.urls import path 
from . import views

urlpatterns = [

    path("", views.base, name="base"),
    path("haramfunc", views.haramfunc, name="haramfunc"),
    path("banglefunc", views.banglefunc, name="banglefunc"),
    path("chainfunc", views.chainfunc, name="chainfunc"),
    path("liked", views.haramfunc, name="liked"),    
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("wishlists/<id>/", views.wishlists, name="wishlists"),
    path("display", views.display, name="display"),
    path("search", views.search, name="search"),

]