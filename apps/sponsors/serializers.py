from rest_framework import serializers
from apps.sponsors.models import StudentSponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ['sponsor', 'amount']
        exclude = ('student',)

class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ['student', 'amount']
        exclude = ('sponsor',)