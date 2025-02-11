import string
import random
from django.core.cache import cache

from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
# from apps.authentication.eskiz_uz import EskizUz
from apps.users.models import CustomUser
# from config.settings import EMAIL, PASSWORD

# eskiz = EskizUz(email=EMAIL, password=PASSWORD)

def send_code(phone_number, message):
    # print(f'Sending code to {phone_number}, message: {message}')
    # message = 'Bu Eskiz dan test'
    # eskiz.send_message(message=message, phone_number=phone_number)
    print(f'Sending code to {phone_number}, message: {message}')
    print(phone_number, message)
    return phone_number




class LoginSerializer(serializers.Serializer):

    code = serializers.IntegerField(write_only=True, required=True)
    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def validate(self, attrs):

        code = attrs.get('code')
        request = self.context.get('request')

        phone_number = cache.get(f'phone_number_{code}')
        cache_code = cache.get(f'code_{phone_number}')

        if code != cache_code:
            raise serializers.ValidationError({'code': 'Noto‘g‘ri yoki eskirgan kod.'})

        user, created = CustomUser.objects.get_or_create(phone_number=phone_number)

        refresh_token = RefreshToken.for_user(user)
        attrs['refresh_token'] = str(refresh_token)
        attrs['access_token'] = str(refresh_token.access_token)

        request.session['refresh_token'] = attrs['refresh_token']

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


class UserLogoutSerializer(serializers.Serializer):

    def validate(self, attrs):
        """
         this is
        """
        request = self.context.get('request')
        if request is None:
            raise ValidationError({'error': 'Request object is missing from context.'})

        if not hasattr(request, 'session'):
            raise ValidationError({'error': 'Session object is not available in request.'})

        refresh_token = request.session.get('refresh_token')
        if not refresh_token:
            raise ValidationError({'token': 'it is enable in session'})

        self.token = refresh_token

        return attrs



    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('token failed')

        request = self.context.get('request')

        request.session.pop('refresh_token', None)

