# from django.contrib.auth import authenticate
from django.core.cache import cache
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import CustomUser
import random
import string


def send_code(phone_number, message):

    print(f'Sending code to {phone_number}, message: {message}', type(message))
    return phone_number




class LoginSerializer(serializers.Serializer):

    code = serializers.IntegerField(write_only=True, required=True)
    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        code = attrs.get('code')

        phone_number = cache.get(f'phone_number_{code}')
        cache_code = cache.get(f'code_{phone_number}')

        if code != cache_code:
            raise serializers.ValidationError({'code': 'Noto‘g‘ri yoki eskirgan kod.'})

        user, created = CustomUser.objects.get_or_create(phone_number=phone_number)

        refresh_token_user = RefreshToken.for_user(user)
        attrs['refresh_token'] = str(refresh_token_user)
        attrs['access_token'] = str(refresh_token_user.access_token)
        cache.set(f'refresh_token_{phone_number}', attrs['refresh_token'])
        cache.set(f'access_token_{phone_number}', attrs['access_token'])

        cache.delete(f'phone_number_{code}')
        cache.delete(f'code_{phone_number}')


        return attrs


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        required=True,
        write_only=True,
    )
    code = serializers.IntegerField(
        read_only=True,
    )


    def save(self,*args, **kwargs):
        phone_number = self.validated_data.get('phone_number')
        # code = ''.join(random.sample(string.ascii_letters + string.digits, 6))
        code = random.randint(100000, 999999)
        send_code(phone_number, message=f'Code: {code}')
        cache.set(f'code_{phone_number}', code, timeout=100 * 60 )
        cache.set(f'phone_number_{code}', phone_number, timeout=100 * 60)


# class UserLogoutSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(required=False)




