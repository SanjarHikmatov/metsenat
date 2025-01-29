from rest_framework import serializers
from django.conf import settings

from apps.users.models import CustomUser

from apps.sponsors.models import StudentSponsor

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ['sponsor', 'amount']

class StudentSerializer(serializers.ModelSerializer):
    sponsors = SponsorSerializer(many=True, read_only=True)
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'sponsors', 'student_dee']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name',
                  'user_type', 'phone_number', 'role',
                  'university', 'student_degree',
                  'available', 'balance',
                  ]



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'password',
                  'user_type', 'phone_number', 'role',
                  'contract_amount', 'university', 'student_degree',
                  'available', 'balance', 'status', 'photo'
                  ]



"""
from rest_framework import serializers
from apps.users.models import CustomUser


class CustomTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        user = CustomUser.objects.filter(phone_number=phone_number).first()

        if user and user.check_password(password):
            return {'user': user}

        raise serializers.ValidationError('Invalid phone number or password.')

"""