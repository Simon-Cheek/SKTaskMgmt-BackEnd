from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserTokenObtainPairSerializer, UserTokenRefreshSerializer

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

class UserTokenRefreshView(TokenRefreshView):
    serializer_class = UserTokenRefreshSerializer
