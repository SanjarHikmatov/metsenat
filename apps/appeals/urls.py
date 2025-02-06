from django.urls import path
from apps.appeals.views import AppealListCreateAPIView,AppealRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', AppealListCreateAPIView.as_view(), name='appeal-list'),
    path('update/<str:pk>/', AppealRetrieveUpdateDestroyAPIView.as_view(), name='appeal-update'),

]