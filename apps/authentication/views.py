from django.contrib.auth import logout
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.serializers import LoginSerializer


class UserLoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def perform_create(self, request, *args, **kwargs):
        pass


class UserLogoutAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response({'error': 'invalid token or already logged out'},status=status.HTTP_401_UNAUTHORIZED)

        logout(request)
        return Response({"message": 'successfully logged out'},status=status.HTTP_200_OK)