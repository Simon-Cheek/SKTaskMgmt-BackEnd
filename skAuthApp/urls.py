from django.urls import path
from .views import UserTokenObtainPairView, UserTokenRefreshView, LogoutView

urlpatterns = [
    path("login/", UserTokenObtainPairView.as_view(), name="login"),
    path("refresh/", UserTokenRefreshView.as_view(), name="refresh"),
    path("logout/", LogoutView.as_view(), name="logout")
]
