from apps.authentication import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginAPIViews.as_view(), name='login'),
]