from apps.general.models import University, PaymeMethod
from apps.general.serializers import UniversitySerializer, PaymeMethodSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class UniversityListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filterset_fields = ['name']

class UniversityCreateAPIView(generics.CreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDeleteAPIView(generics.DestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class PaymentMethodListAPIView(generics.ListAPIView):
    queryset = PaymeMethod.objects.all()
    serializer_class = PaymeMethodSerializer
    filterset_fields = ['name']

class PaymentMethodCreateAPIView(generics.CreateAPIView):
    queryset = PaymeMethod.objects.all()
    serializer_class = PaymeMethodSerializer

class PaymentMethodUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = PaymeMethod.objects.all()
    serializer_class = PaymeMethodSerializer


class PaymentMethodDeleteAPIView(generics.DestroyAPIView):
    queryset = PaymeMethod.objects.all()
    serializer_class = PaymeMethodSerializer




