from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer, UserDetailSerializer




class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('-created_at')
    serializer_class = UserSerializer

    filterset_fields = {
        'university': ['exact'],
        'user_type': ['exact'],
        'role': ['exact'],
        'balance': ['gte', 'lte'],
        'available': ['gte', 'lte'],
        'student_degree': ['exact'],

    }

    search_fields = ['first_name','last_name','phone_number']

    ordering_fields = [
        'first_name','last_name',
        'phone_number', 'balance',
        'available', 'status',
        'university']


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all().order_by('-created_at')
    serializer_class = UserDetailSerializer














