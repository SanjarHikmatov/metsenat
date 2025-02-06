from rest_framework import serializers

from apps.general.service import allocate_founds
from apps.sponsors.models import StudentSponsor
from apps.general.service import validate_student_sponsor_balance



class StudentSponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ['sponsor', 'student', 'amount',]


    def validate(self, data):
        """
            This function validates the balances of the sponsor and the student.
            Here, I have used the validate_student_sponsor_balance() function,
            which is written in the general service.py file.
        """

        amount = data.get('amount')
        sponsor = data.get('sponsor')
        student = data.get('student')

        validate_student_sponsor_balance(sponsor, student, amount)

        return data


    def create(self, validated_data):
        """
        This function transfers the amount allocated by the sponsor to the student
        from the sponsor's appeal to the student's available balance.
        It utilizes the allocate_fund function from service.py in the general module.
        """
        sponsor = validated_data.get('sponsor')
        student = validated_data.get('student')
        amount = validated_data.get('amount')

        allocate_founds(sponsor, student, amount)

        return StudentSponsor.objects.create(**validated_data)


class StudentSponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ['id','sponsor','student', 'amount',]

        sponsor = serializers.PrimaryKeyRelatedField(queryset=StudentSponsor.objects.order_by('-created_at'))
        student = serializers.PrimaryKeyRelatedField(read_only=True)
