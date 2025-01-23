from requests import Response
from rest_framework import generics

from apps.appeals.serializers import AppealSerializer
from apps.appeals.models import Appeal
from rest_framework.views import APIView
from rest_framework.response import Response



class AppealListAPIView(APIView):

    def get(self, request):
        appeals = Appeal.objects.all()
        serializer = AppealSerializer(appeals, many=True)
        return Response(serializer.data)


class AppealCreateAPIView(generics.CreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

class AppealUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

class AppealDeleteAPIView(generics.DestroyAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer



