from django.urls import path

from apps.sponsors.views import (
    StudentSponsorListCreateAPIView,
    StudentSponsorDeleteAPIView,
    StudentSponsorUpdateAPIView,
)

urlpatterns = [
    path('', StudentSponsorListCreateAPIView.as_view(), name='sponsor-list'),
    path('update/<str:pk>', StudentSponsorUpdateAPIView.as_view(), name='sponsor-update'),
    path('delete/<str:pk>', StudentSponsorDeleteAPIView.as_view(), name='sponsor-delete'),
]