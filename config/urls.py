
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # =========== admin ===============
    path('admin/', admin.site.urls),

    # ============ Appeal urls =======================================
    path('appeals/', include('apps.appeals.urls'), name='appeals'),

    # ============= Student urls ===============================
    path('users/', include('apps.users.urls'), name='users'),

    # ============= generals include urls ==============================
    path('generals/', include('apps.general.urls'), name='generals'),

    # ================ student sponsor ==================================================
    path('student_sponsors/', include('apps.sponsors.urls'), name="student_sponsors"),

    # ====================== authentication ======================================
    path('auth/', include('apps.authentication.urls'), name='token_api_login'),

]
