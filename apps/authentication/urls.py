from django.urls import path

from apps.authentication.views import (
    UserLogoutAPIView,
    SendAuthCodeAPIView,
    AuthCodeConfirmAPIView)
urlpatterns = [
    path('send-auth-code/', SendAuthCodeAPIView.as_view(), name='send-code'),
    path('login/', AuthCodeConfirmAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),

]

