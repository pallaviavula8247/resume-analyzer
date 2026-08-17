from django.contrib import admin

from .models import User


# =========================================================
# CUSTOM USER ADMIN
# =========================================================

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
        "phone",
        "is_active",
        "is_staff",
        "date_joined",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    list_filter = (
        "is_active",
        "is_staff",
    )

    ordering = (
        "-date_joined",
    )

