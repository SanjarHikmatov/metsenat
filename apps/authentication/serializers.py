from rest_framework import serializers
from apps.general.validation_call_number import uzb_phone_number_validators


class RegisterSerializer(serializers.Serializer):

    phone_number = serializers.CharField(
        validators=uzb_phone_number_validators,
        widget=serializers.CharField(
            attrs={
                'class': 'form-control',
                "placeholder": "Phone number",
            }
        )
    )

    user_code = serializers.CharField(required=False)

