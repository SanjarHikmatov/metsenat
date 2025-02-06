from django.contrib import admin
from apps.appeals.models import Appeal

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    pass


