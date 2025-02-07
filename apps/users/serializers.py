from rest_framework import serializers

from apps.users.models import CustomUser




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

        """
           Custom validation for user role-related fields.
           Ensures that required fields are provided based on the selected user role
           and that unnecessary fields are not included.
        """

        user_role = attrs['role']
        student_university = attrs['university']
        student_degree = attrs['student_degree']
        user_type = attrs['type']

        # If the user is a student, they must provide a university.
        if user_role == CustomUser.Role.STUDENT and not student_university:
            raise serializers.ValidationError({'university': 'This field required.'})

        # If the user is a student, their degree cannot be 'empty' and must be either 'bachelor' or 'master'.
        if user_role == CustomUser.Role.STUDENT and student_degree == CustomUser.StudentDegree.EMPTY:
            raise serializers.ValidationError({'student degree': 'This field will be bachelor or master.'})

        # If the user is a student, they cannot have a user type of 'juridic' or 'physical'.
        if user_role == CustomUser.Role.STUDENT and user_type in ['juridic', 'physical']:
            raise serializers.ValidationError({'user type': 'you can not add this field.'})

        # If the user is a sponsor, they should not have university or student degree fields set.
        if user_role == CustomUser.Role.SPONSOR and student_university:
            raise serializers.ValidationError({'university or student degree': 'you can not add university or student degree.'})

        if user_role == CustomUser.Role.SPONSOR and student_degree in ['bachelor', 'master']:
            raise serializers.ValidationError({'university or student degree': 'you can not add university or student degree.'})

        # If the user is a sponsor, they must provide a user type.
        if user_role == CustomUser.Role.SPONSOR and not user_type:
            raise serializers.ValidationError({'user type': 'This field required.'})

        # If the user is an admin, they should not have university or student degree fields set.
        if user_role == CustomUser.Role.ADMIN and student_university:
            raise serializers.ValidationError({'university or student degree': 'you can not add university or student degree.'})

        if user_role == CustomUser.Role.ADMIN and student_degree in ['bachelor', 'master']:
            raise serializers.ValidationError({'user type': 'This field required.'})

        if user_role == CustomUser.Role.ADMIN and user_type in ['juridic', 'physical']:
            raise serializers.ValidationError({'user type': 'you can not add this field.'})

        return attrs


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'password',
                  'type', 'phone_number', 'role',
                   'university', 'student_degree',
                  'available', 'balance','photo'
                  ]



