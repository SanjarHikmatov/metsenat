from django.contrib.auth import authenticate
from rest_framework import generics, views, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.appeals.models import Appeal
from apps.appeals.serializers import AppealSerializer
from django_filters.rest_framework import DjangoFilterBackend



class AppealListAPIView(generics.ListAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    filterset_fields = ['organization','amount','phone_number',
                        'is_verified','pay_method',
                        ]


class AppealCreateAPIView(generics.CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer


class AppealUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer


class AppealDeleteAPIView(generics.DestroyAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer





