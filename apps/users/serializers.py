from rest_framework import serializers

from apps.appeals.models import Appeal
from apps.users.models import CustomUser
from apps.general.service import validate_user




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name',
                  'type', 'phone_number', 'role',
                  'university', 'student_degree',
                   'balance','available',
                  ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'available',]


    def validate(self, attrs):
        return validate_user(attrs)


