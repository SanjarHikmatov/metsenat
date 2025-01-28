from django.urls import path
from apps.general.views import (
    PaymentMethodListAPIView,
    PaymentMethodCreateAPIView,
    PaymentMethodUpdateAPIView,
    PaymentMethodDeleteAPIView,
    UniversityListAPIView,
    UniversityUpdateAPIView,
    UniversityDeleteAPIView, UniversityCreateAPIView,
)

urlpatterns = [
# ============= payment method urls ===============
    path('payment', PaymentMethodListAPIView.as_view(), name='payment-list'),
    path('payment_create/', PaymentMethodCreateAPIView.as_view(), name='payment-create'),
    path('payment_update/<str:pk>/', PaymentMethodUpdateAPIView.as_view(), name='payment-update'),
    path('payment_delete/<str:pk>/', PaymentMethodDeleteAPIView.as_view(), name='payment-delete'),

    # ================= university urls =================
    path('university', UniversityListAPIView.as_view(), name='university-list'),
    path('university_create/', UniversityCreateAPIView.as_view(), name='university-create'),
    path('university_update/<str:pk>/', UniversityUpdateAPIView.as_view(), name='university-update'),
    path('university_delete/<str:pk>/', UniversityDeleteAPIView.as_view(), name='university-delete'),

]