from django.urls import path

from apps.sponsors.views import (
    StudentSponsorCreateAPIView,
    StudentSponsorListAPIView,
    StudentSponsorDeleteAPIView,
    SponsorUpdateAPIView,
)

urlpatterns = [
    path('', StudentSponsorListAPIView.as_view(), name='sponsor-list'),
    path('create_api/', StudentSponsorCreateAPIView.as_view(), name='sponsor-create'),
    path('update/<str:pk>', SponsorUpdateAPIView.as_view(), name='sponsor-update'),
    path('delete/<str:pk>', StudentSponsorDeleteAPIView.as_view(), name='sponsor-delete'),
]