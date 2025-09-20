from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

# Use custom User model defined in skUserApp
User = get_user_model()

# Override Token Obtaining to include user info in response
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add user info as needed here
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
        }
        return data

# Override Token Refresh to return user info in response
class UserTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Decode the refresh token to get user ID
        refresh = RefreshToken(attrs['refresh'])
        user_id = refresh.access_token['user_id']  # comes from the token payload

        # Fetch full user object to include in response
        u = User.objects.get(id=user_id)

        data["user"] = {
            "id": u.id,
            "username": u.username,
            "email": u.email,
        }
        return data
