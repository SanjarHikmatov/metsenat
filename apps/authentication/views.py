from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from apps.authentication.serializers import RegisterSerializer
import random
class UserRegisterView(views.APIView):
    def admin_code(self):
        return str(random.randint(1000, 9999))

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(commit=False):
            user_code = serializer.validated_data['user_code']
            if user_code  is self.admin_code:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

