from django.urls import path
from .views import UserTokenObtainPairView, UserTokenRefreshView

urlpatterns = [
    path("token/", UserTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", UserTokenRefreshView.as_view(), name="token_refresh"),
]
