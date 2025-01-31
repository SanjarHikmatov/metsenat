"""# import random
# import string
#
# from rest_framework import views, status
# from rest_framework.response import Response
#
# from apps.authentication.models import OTP
# from apps.authentication.serializers import LoginRegisterSerializer
#
# def generate_otp():
#     return ''.join(random.sample(string.ascii_letters + string.digits, 6))
#
#
#
#
# class LoginRegisterAPIView(views.APIView):
#
#     def post(self, request, *args, **kwargs):
#         serializer = LoginRegisterSerializer(data=request.data)
#         phone_number = serializer.data['phone_number']
#
#         if not phone_number:
#             return Response({'phone_number':'You should enter phone number'},status=status.HTTP_400_BAD_REQUEST)
#
#         if phone_number:
#
#             otp_code = generate_otp()
#
#             inspect, created, = OTP.objects.get_or_create(
#                 phone_number=phone_number,
#                 defaults={'code': otp_code}
#             )
#
#             # ==== we need write some code for send login code =======
#             send_code = (phone_number, otp_code)
#
#             return Response({'otp_code': 'Code send successfully'}, status=status.HTTP_200_OK)
#         return Response({'otp_code': 'Code send failed'}, status=status.HTTP_400_BAD_REQUEST)
"""
from django.contrib.auth import authenticate
from rest_framework import views
from rest_framework import exceptions
from rest_framework.response import Response


class LoginAPIViews(views.APIView):
    def post(self, request, *args, **kwargs):
        username, password = request.data['username'], request.data['password']
        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise exceptions.AuthenticationFailed('invalid username or password')
            from rest_framework.authtoken.models import Token
            token_obj, _ = Token.objects.get_or_create(user=user)

        else:
            raise exceptions.AuthenticationFailed('invalid username or password')
        return Response({'token': token_obj.key})

