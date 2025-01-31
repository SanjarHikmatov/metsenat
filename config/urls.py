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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ============ Appeal urls ===============
    path('appeals/', include('apps.appeals.urls'), name='appeals'),

    # ============= Student urls ===================
    path('users/', include('apps.users.urls'), name='users'),

    # ============= generals include urls ===============

    path('generals/', include('apps.general.urls'), name='generals'),

    path('student_sponsors/', include('apps.sponsors.urls'), name="student_sponsors"),
    path('token_api_login', include('apps.authentication.urls'), name='token_api_login'),
]
