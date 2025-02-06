from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    filter_horizontal = []

    readonly_fields = ()
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
                    "is_superuser",
                    "is_staff",
                    "role",
                ),
            },
        ),
        # (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        # ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )
    list_display = ("phone_number", "first_name", "last_name", "role")
    list_filter = ("role",)
    search_fields = ("first_name", "last_name", "phone_number", "role")
    ordering = ("phone_number",)
