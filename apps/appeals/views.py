from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from apps.appeals.models import Appeal
from apps.appeals.serializers import AppealSerializer, AppealUpdateSerializer



class AppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appeal.objects.order_by('-created_at')
    serializer_class = AppealSerializer
    filterset_fields = {
        'amount': ['gte', 'lte'],
        'created_at': ['lte', 'gte'],
        'is_verified': ['exact'],
        'pay_method': ['exact'],
        'sponsor': ['exact'],
        'available': ['gte', 'lte'],
        }

    search_fields = ['full_name','phone_number']

    ordering_fields = [
        'full_name', 'amount'
        'phone_number', 'sponsor',
        'created_at', 'is_verified',
        'pay_method', 'university'
        'available', 'status',
        ]
    pagination_class = LimitOffsetPagination

class AppealRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appeal.objects.order_by('-created_at')
    serializer_class = AppealUpdateSerializer

    filterset_fields = {
        'amount': ['gte', 'lte'],
        'created_at': ['lte', 'gte'],
        'is_verified': ['exact'],
        'pay_method': ['exact'],
        'sponsor': ['exact'],
        'available': ['gte', 'lte'],
    }

    search_fields = ['full_name', 'phone_number']

    ordering_fields = [
        'full_name', 'amount'
        'phone_number', 'sponsor',
        'created_at', 'is_verified',
        'pay_method', 'university'
        'available', 'status',
    ]






