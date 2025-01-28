from rest_framework import generics
from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer, UserDetailSerializer




class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    filterset_fields = ['first_name',
                        'last_name',
                        'phone_number',
                        'status',
                        'available',
                        ]
    search_fields = ['first_name',
                     'last_name',
                     'phone_number',
                     'created_at',
                     'available',
                     'status',
                     ]

    ordering_fields = ['first_name',
                       'last_name',
                        'phone_number',
                       'status',
                       'available',
                       'balance',
                       ]






class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all().order_by('-pk')
    serializer_class = UserDetailSerializer










