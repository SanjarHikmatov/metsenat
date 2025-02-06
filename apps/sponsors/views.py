from rest_framework.response import Response
from rest_framework import generics, status, serializers

from apps.sponsors.models import StudentSponsor
from apps.sponsors.serializers import StudentSponsorCreateSerializer, StudentSponsorUpdateSerializer


class StudentSponsorListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.order_by('-created_at')
    serializer_class = StudentSponsorCreateSerializer



class StudentSponsorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorUpdateSerializer



class StudentSponsorDeleteAPIView(generics.DestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorCreateSerializer


