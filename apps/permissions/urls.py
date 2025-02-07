from apps.permissions.views import UserPermissionListAPIView
from django.urls import path

urlpatterns = [
    path('me/', UserPermissionListAPIView.as_view(), name='permission-list'),
]