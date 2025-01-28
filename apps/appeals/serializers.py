from rest_framework import serializers
from apps.appeals.models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = [
            'full_name',
            'phone_number',
            'is_verified',
            'pay_method',
            'amount',
            'organization',
        ]


