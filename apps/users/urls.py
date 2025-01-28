from django.urls import path
from apps.users.views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView
)





urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list'),
    path('detail/<str:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='student-retrieve'),

]
