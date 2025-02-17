from rest_framework import serializers
from apps.appeals.models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id','created_at','updated_at','status','amount', 'sponsor', 'phone_number', 'pay_method']
        read_only_fields = ('id','created_at','updated_at', 'status', )





class AppealUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'created_at', 'updated_at', 'status', 'amount', 'sponsor',
                  'phone_number', 'pay_method']
        read_only_fields = ('id', 'created_at', 'updated_at',)



