# views.py
from rest_framework.permissions import AllowAny
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

    def post(self, request, *args, **kwargs):
        data = request.data.copy()  # make mutable copy

        if "refresh" not in data:
            refresh_token = request.COOKIES.get(REFRESH_TOKEN_COOKIE)
            if not refresh_token:
                return Response({"detail": "No refresh token"}, status=400)
            data["refresh"] = refresh_token

        # Re-wrap the request with the modified data
        request._full_data = data

        # Now just let the parent view do its thing
        return super().post(request, *args, **kwargs)

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie(
            REFRESH_TOKEN_COOKIE,
            path="/",
            samesite="Lax",
        )
        return response
