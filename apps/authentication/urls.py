from django.urls import path

from apps.authentication.views import (
    UserLogoutAPIView,
    SendAuthCodeAPIView,
    AuthCodeConfirmAPIView)

urlpatterns = [
    path('login/', AuthCodeConfirmAPIView.as_view(), name='login'),
    path('send-auth-code/', SendAuthCodeAPIView.as_view(), name='send-code'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),

]