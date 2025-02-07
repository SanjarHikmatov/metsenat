from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from django.contrib.auth.models import Permission

from apps.permissions.serializer import UserPermissionListSerializer


class UserPermissionListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPermissionListSerializer

    def get_queryset(self):
        user = self.request.user
        perms = user.get_all_permissions()
        return perms