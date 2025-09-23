# views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserTokenObtainPairSerializer, UserTokenRefreshSerializer
from rest_framework.views import APIView

REFRESH_TOKEN_COOKIE = "skTaskMgmt-Refresh"

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data

        # Put refresh token in HttpOnly cookie
        refresh = data.get("refresh")
        if refresh:
            response.set_cookie(
                key=REFRESH_TOKEN_COOKIE,
                value=refresh,
                httponly=True,
                secure=True,       # True in production (HTTPS only)
                samesite="Lax",    # Or "Strict" if you prefer
                max_age=7*24*60*60 # match token lifetime, e.g. 7 days
            )
            # Optionally remove from response body
            del data["refresh"]

        return response

class UserTokenRefreshView(TokenRefreshView):
    serializer_class = UserTokenRefreshSerializer

class LogoutView(APIView):
    def post(self, request):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie(
            REFRESH_TOKEN_COOKIE,
            path="/",
            samesite="Lax",
        )
        return response
