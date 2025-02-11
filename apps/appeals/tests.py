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

# # Token yaratish uchun ma'lumotlar
# payload = {
#     'user_id': 123,
#     'jti': str(uuid.uuid4()),  # Yagona identifikator (JTI)
#     'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # Token muddati
# }
# 
# # Maxfiy kalit
# secret_key = 'your_secret_key'
# 
# # JWT yaratish
# token = jwt.encode(payload, secret_key, algorithm='HS256')
# 
# print(f"Yaratilgan token: {token}")
# # Tokenni tekshirish va o'qish
# decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
# 
# # JTI ni olish
# jti = decoded_token.get('jti')
# exp = decoded_token.get('exp')
# 
# print(f"Tokenning JTI identifikatori: {jti}")
# print({exp})


#==============================
# -----BEGIN RSA PRIVATE KEY-----
# MIIEowIBAAKCAQEApRQVh8bItHZvZt5pOGSzj+YNl+LKVqd6HoY+lQ/7wpVPkLQQ
# lzYLvdjQ33rqs6QsJ5SI7eSJo/cVjwT0yImKv/fszaRQFxsbC7zqLlGMYR333K+g
# H9maK30lLvnhGxTbSdeTPn0ldyrh/9zvUdn4Y4+gkEf6RnqUEB/EYp68Tfu6bjWA
# M8nybNIi/UXn63JoB0yYLbWiC485IFUn+7ZLIVw3P9P2uYOCOOBeD4XxUd6SC6SZ
# l/rIe5HPrp1l2QwFfEiMBmdU1BO67ktRAd37VLx9fRrv6zWEqwTZ/XaxYTmVY6ED
# JABCO2w+7oyUP/ee7J2OqQEjKZmmVokuScOJZQIDAQABAoIBAG2pOeRImWvIgZjE
# hwF/ZAljugP8FI4cE3PTmh9LzuMkbQajl6HbtVEYhyjubpuHpA1nDs950jWqHhg0
# IqhVNmbwO88gKFQxHXZeuPKsGaUqU023HZgK5e+d4uWh+XgUEtiq7JXGbO0M/7UI
# /7JQKkF5WCCAsDHBnDpZ4AvjhxQF5C5fk1QIUl1RH93e2XYhChR7BPlBCrWCd7Jr
# l5TtWDBNjGCuJOpO9J0Lt/SnymAf+W4nFLJYBtZpKYVYb32ege5ekHXCvQ9ZMIAc
# FPiAAmzfaM2ZcjYSxW8MISw0lX45ff+FcKFjTZoQorBhwqsqB2Ii3ypkfqv35LQX
# TJNEngECgYEA1avMwvlKAfdjWUNlUD+3TIjpuSV0HbHKn6v7l85UhUNi4Pfl4RnQ
# 7d0Hf2+3Pux9djC8DShteMtZrgoo68+TpKj5TPmbVhCV9rZ6bIzi6Q6YuXqHXAE6
# sq39pU2hBOcLNJIPYw7bZDgsmF/jVWD61fl/2YcKJiIOvULnidFwXokCgYEAxcfw
# HVw1AvW91ZYiIA/eGuWQumin2yaad3Y2UTuPO2QCM0rg+VllD7mlYHToMvYEqb5N
# 2/l/PSnGSpPKcK/qOKuahQW4yR/AAHh4nNUyzGN7mxn9bB6jETOWTgpPB+jULLzZ
# sSpiNx/0TyXrpnl9wgKUVrB6psCo0y3PXOeePP0CgYEAtiCoepDvCloKbu3Jj+uf
# nDcfsddA8Ia5hfycibsvxB+6SrRDV+ofcoDygSeCdLoz/uhvgm+xUENU/8pdMxNO
# cA4v4fLo+yVMDm1gUOKOD8WHXKIaesv5cpBoIdzXoUwm+vp87xyc2QIg0Qj6x63Q
# YU84MPywI+znz18V6R2CwLECgYBIAxJkPkx29W7XM8DdF6nw9SELHkvvuVCIqpwA
# W8U9BJ7geiUL5QatARU715Ur6POtskK7E07GwE0YnlMZUJPhamnqgTjU0iCgizyv
# Ldk/HgHFaWMiWM1a2AOkCpDX+mg2mdRRc3MrSxEzOEVi6d1mJHZKUht2V7OgoI9d
# 7l9pKQKBgDzFqsHemCDnVW5kk0QvGKoyG7ZCNHgsDG1FKRaU5QP3qnZUn/8T6HKU
# MhG6eCZP7esQpYqkmwJMSijeSJw7D0f/s0QzH1boKoL2B/jkWVh6DqlhG5itA6U8
# I805vBi/1xfMrrilZQ0YJC/SM0tPrxuPFnCmfXiqk0GaLWforsO2
# -----END RSA PRIVATE KEY-----
#
