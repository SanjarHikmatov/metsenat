from rest_framework_simplejwt.views import TokenObtainPairView

# from apps.authentication import views
from django.urls import path

from apps.authentication.views import UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    # path('login/', views.LoginAPIViews.as_view(), name='login'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),

]