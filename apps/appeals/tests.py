# from django.test import TestCase
#
# # Create your tests here.
# import jwt
# import datetime
#
# # Token yaratish uchun ma'lumotlar
# payload = {
#     'user_id': 123,
#     'TOKEN_TYPE_CLAIM': 'access_token',  # Token turi
#     'exp': datetime.datetime.now()+ datetime.timedelta(minutes=5)  # Muddati
# }
#
# # Maxfiy kalit
# secret_key = 'your_secret_key'
#
# # JWT yaratish
# token = jwt.encode(payload, secret_key, algorithm='HS256')
# print(f"Yaratilgan token: {token}")
#
# # Tokenni tekshirish va o'qish
# decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
#
# # Token turi va foydalanuvchi ID sini chiqarish
# token_type = decoded_token.get('TOKEN_TYPE_CLAIM')
# user_id = decoded_token.get('user_id')
#
# print(f"Token turi: {token_type}")
# print(f"Foydalanuvchi ID: {user_id}")
# pip install jwt

import jwt
import uuid
import datetime

# Token yaratish uchun ma'lumotlar
payload = {
    'user_id': 123,
    'jti': str(uuid.uuid4()),  # Yagona identifikator (JTI)
    'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # Token muddati
}

# Maxfiy kalit
secret_key = 'your_secret_key'

# JWT yaratish
token = jwt.encode(payload, secret_key, algorithm='HS256')

print(f"Yaratilgan token: {token}")
# Tokenni tekshirish va o'qish
decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])

# JTI ni olish
jti = decoded_token.get('jti')
exp = decoded_token.get('exp')

print(f"Tokenning JTI identifikatori: {jti}")
print({exp})
