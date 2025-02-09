
from django.contrib import admin
from django.urls import path, include
# =================== there for swagger ======================
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Metsenat API",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
   public=True,
   permission_classes=[permissions.AllowAny]
)


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

    path('permissions/', include('apps.permissions.urls'), name='permissions'),

    #==================== this url for swagger ==================================
    path("swagger/", schema_view.with_ui("swagger"), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]
