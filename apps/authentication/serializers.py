from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.general.validation_call_number import uzb_phone_number_validators
from apps.users.models import CustomUser
import random
import string

def generate_otp():
    return ''.join(random.sample(string.ascii_letters + string.digits, 6))


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, validators=[uzb_phone_number_validators])
    password = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)


    def validate(self, attrs):

        phone_number = attrs.get('phone_number')
        if not phone_number:
            raise serializers.ValidationError({'phone number': 'Phone number required'})
        otp = generate_otp()
        inspect, created, = CustomUser.objects.get_or_create(
            phone_number=phone_number,
            defaults={'password': otp}
        )
        refresh_token = RefreshToken.for_user(inspect)
        attrs['refresh'] = str(refresh_token)
        attrs['access'] = str(refresh_token.access_token)

        return attrs

