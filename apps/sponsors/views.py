from decimal import Decimal

from django.db.models import F
from rest_framework.response import Response
from rest_framework import views, generics, status, serializers

from apps.general.models import University
from apps.sponsors.models import StudentSponsor
from apps.sponsors.serializers import StudentSponsorSerializer, StudentSponsorUpdateSerializer
from apps.users.models import CustomUser


class StudentSponsorListAPIView(generics.ListAPIView):
    queryset = StudentSponsor.objects.order_by('-created_at')
    serializer_class = StudentSponsorSerializer


class  StudentSponsorCreateAPIView(generics.CreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):

        amount = serializer.validated_data['amount']
        sponsor = serializer.validated_data['sponsor']
        student = serializer.validated_data['student']

        sponsor_available = sponsor.available
        student_available = student.available
        student_balance = student.balance

        if amount > sponsor_available:
            raise serializers.ValidationError({'sponsor_balance': 'This is more then sponsor available balance'})

        if amount > student_available:
            raise serializers.ValidationError({'student_contract': 'This is more then student available balance'})
        elif amount <= student_available:
            student_available += amount
            if student_balance < student_available:
                excess_money = student_available + amount
                raise serializers.ValidationError(
                    {'excess_money': f'this added amount exceeded the student contract This is {excess_money}'}
                )
        else:
            student_available += amount

        sponsor.available -= amount
        student.available = student_available
        sponsor.save()
        student.save()
        serializer.save()


class StudentSponsorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        instance = self.get_object()
        sponsor = serializer.validated_data['sponsor']
        amount = serializer.validated_data['amount']
        sponsor_available = sponsor.available

        if amount and sponsor_available > amount and sponsor_available > 0:
            sponsor_av_amount = sponsor_available + instance
            if sponsor_av_amount < amount:
                raise serializers.ValidationError({'sponsor_available': 'This is more then sponsor available balance'})
            sponsor_available -= amount

        sponsor.save()
        amount.save()
        serializer.save()



class StudentSponsorDeleteAPIView(generics.DestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer




