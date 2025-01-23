from rest_framework.response import Response
from rest_framework import views, generics
from apps.sponsors.models import StudentSponsor
from apps.sponsors.serializers import StudentSponsorSerializer


class SponsorViewList(views.APIView):

    def get(self, request):
        sponsors = StudentSponsor.objects.order_by('id')
        serializer = StudentSponsorSerializer(sponsors, many=True)
        return Response(serializer.data)


class SponsorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer


class SponsorDeleteAPIView(generics.DestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

class StudentListAPIView(views.APIView):
    def get(self, request):
        students = StudentSponsor.objects.order_by('id')
        serializer = StudentSponsorSerializer(students, many=True)
        return Response(serializer.data)
class StudentCreateAPIView(generics.CreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

class StudentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

class StudentDeleteAPIView(generics.DestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer



