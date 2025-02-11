from django.urls import path

from apps.users.views import UserListCreateAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list'),
]
