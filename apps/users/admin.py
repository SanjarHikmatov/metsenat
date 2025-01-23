from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import CustomUser
# from django.utils.translation import gettext_lazy as _

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    readonly_fields = (
        "last_login",
        "date_joined",
    )
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (
            # _("Personal info"),
            "Personal info",
            {
                "fields":
                    (
                        "first_name",
                        "last_name",
                        "photo"
                    )
            }
        ),
        (
            # _("Permissions",)
              "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "role",
                ),
            },
        ),
        # (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "usable_password", "password1"),
            },
        ),
    )
    list_display = ("phone_number", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "phone_number", "role")
    ordering = ("phone_number",)
