from rest_framework import generics
from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer, UserDetailSerializer




class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    filterset_fields = ['first_name', 'last_name','phone_number']
    search_fields = ['first_name','last_name',]

    ordering_fields = ['first_name','last_name',]


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all().order_by('-created_at')
    serializer_class = UserDetailSerializer














