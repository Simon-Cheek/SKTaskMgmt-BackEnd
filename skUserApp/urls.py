# users/urls.py
from django.urls import path
from .views import UserRegisterView, MeView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("me/", MeView.as_view(), name="me")
]
