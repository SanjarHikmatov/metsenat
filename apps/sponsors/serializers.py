from rest_framework import serializers
from apps.sponsors.models import StudentSponsor



class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ['sponsor', 'student', 'amount',]

class StudentSponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ['id','sponsor','student', 'amount',]

        sponsor = serializers.PrimaryKeyRelatedField(queryset=StudentSponsor.objects.all())
        student = serializers.PrimaryKeyRelatedField(read_only=True)
