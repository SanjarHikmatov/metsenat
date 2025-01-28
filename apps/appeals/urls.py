from django.urls import path
from apps.appeals.views import *

urlpatterns = [
    path('', AppealListAPIView.as_view(), name='appeal-list'),
    path('create/', AppealCreateAPIView.as_view(), name='appeal-create'),
    path('update/<str:pk>/', AppealUpdateAPIView.as_view(), name='appeal-update'),
    path('delete/<str:pk>/', AppealDeleteAPIView.as_view(), name='appeal-delete'),

]