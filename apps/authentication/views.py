from rest_framework import exceptions
from django.contrib.auth import logout
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from yaml import serialize

# from .serializers import UserLogoutSerializer
from apps.authentication.serializers import SendAuthCodeSerializer, LoginSerializer, UserLogoutSerializer


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





class UserLogoutAPIView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserLogoutSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Successfully logged out"}, status=200)
