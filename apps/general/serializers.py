from rest_framework import serializers
from apps.general.models import University, PaymeMethod


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['name','id', 'contract_amount']


class PaymeMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymeMethod
        fields = ['name', 'id']
