from django.urls import path, include
from users import views

urlpatterns = [
    path("create/", views.createUserView.as_view()),
    path("modify/<int:pk>", views.modifyUserView.as_view()),
]