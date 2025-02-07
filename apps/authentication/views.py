from linecache import cache

from rest_framework import exceptions
from django.contrib.auth import logout
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserLogoutSerializer
from apps.authentication.serializers import SendAuthCodeSerializer, LoginSerializer


class AuthCodeConfirmAPIView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def perform_create(self, serializer):
        pass

class SendAuthCodeAPIView(CreateAPIView):
    serializer_class = SendAuthCodeSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()





class UserLogoutAPIView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):

        refresh_token = request.data.get('refresh_token')
        # phone_number = request.data.get('phone_number')

        print(refresh_token)

        if not refresh_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except exceptions.ValidationError:
            return Response({'error': 'invalid token or already logged out'},status=status.HTTP_401_UNAUTHORIZED)

        logout(request)
        return Response({"message": 'successfully logged out'},status=status.HTTP_200_OK)