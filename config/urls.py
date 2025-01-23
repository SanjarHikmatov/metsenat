"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.appeals.views import (
    AppealListAPIView,
    AppealCreateAPIView,
    AppealDeleteAPIView,
    AppealUpdateAPIView
)
from apps.sponsors.views import (
    StudentListAPIView,
    StudentCreateAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
    SponsorDeleteAPIView,
    SponsorUpdateAPIView,
    SponsorViewList
)
from apps.general.views import (
    PaymentMethodListAPIView,
    PaymentMethodCreateAPIView,
    PaymentMethodUpdateAPIView,
    PaymentMethodDeleteAPIView,
    UniversityListAPIView,
    UniversityCreateAPIView,
    UniversityUpdateAPIView,
    UniversityDeleteAPIView,
)
from apps.authentication.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    # ============ Appeal urls ===============
    path('appeals/', AppealListAPIView.as_view(), name='appeal-list'),
    path('appeals/create/', AppealCreateAPIView.as_view(), name='appeal-create'),
    path('appeals/update/<int:pk>/', AppealUpdateAPIView.as_view(), name='appeal-update'),
    path('appeals/delete/<int:pk>/', AppealDeleteAPIView.as_view(), name='appeal-delete'),

    # ============= Student urls ===================
    path('student/', StudentListAPIView.as_view(), name='student-list'),
    path('student/create/', StudentCreateAPIView.as_view(), name='student-list'),
    path('student/update/<int:pk>/', StudentUpdateAPIView.as_view(), name='student-list'),
    path('student/delete/<int:pk>/', StudentDeleteAPIView.as_view(), name='student-list'),

    # =================== sponsor urls ==================
    path('sponsors/', SponsorViewList.as_view(), name='sponsor-list'),
    path('sponsors/update/<int:pk>/', SponsorUpdateAPIView.as_view(), name='sponsor-update'),
    path('sponsors/delete/<int:pk>/', SponsorDeleteAPIView.as_view(), name='sponsor-delete'),

    # ============= payment method ===============
    path('payment/', PaymentMethodListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentMethodCreateAPIView.as_view(), name='payment-create'),
    path('payment/update/<int:pk>/', PaymentMethodUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:pk>/', PaymentMethodDeleteAPIView.as_view(), name='payment-delete'),

    # ================= university urls =================
    path('universty/', UniversityListAPIView.as_view(), name='university-list'),
    path('university/create/', UniversityCreateAPIView.as_view(), name='university-list'),
    path('university/update/<int:pk>/', UniversityUpdateAPIView.as_view(), name='university-update'),
    path('university/delete/<int:pk>/', UniversityDeleteAPIView.as_view(), name='university-delete'),
    path('register/', register, name='register'),

]
