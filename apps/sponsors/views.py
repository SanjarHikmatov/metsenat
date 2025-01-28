from rest_framework.response import Response
from rest_framework import views, generics, status
from rest_framework.views import APIView

from apps.sponsors.models import StudentSponsor
from apps.sponsors.serializers import StudentSponsorSerializer, SponsorUpdateSerializer


class StudentSponsorListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = StudentSponsor.objects.order_by('id')
        serializer = StudentSponsorSerializer(queryset, many=True)
        return Response(serializer.data)

class  StudentSponsorCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StudentSponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SponsorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = SponsorUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentSponsorDeleteAPIView(generics.DestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer




