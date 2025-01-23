from rest_framework.views import APIView
from apps.general.models import University, PaymeMethod
from apps.general.serializers import UniversitySerializer, PaymeMethodSerializer
from rest_framework import generics
from rest_framework.response import Response

class UniversityListAPIView(APIView):

    def get(self, request):
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(serializer.data)

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


class PaymentMethodCreateAPIView(generics.CreateAPIView):
    queryset = PaymeMethod.objects.all()
    serializer_class = PaymeMethodSerializer

class PaymentMethodUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = PaymeMethod.objects.all()
    serializer_class = PaymeMethodSerializer


class PaymentMethodDeleteAPIView(generics.DestroyAPIView):
    queryset = PaymeMethod.objects.all()
    serializer_class = PaymeMethodSerializer




