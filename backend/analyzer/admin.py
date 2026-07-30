from django.contrib import admin
from .models import JobMatch


@admin.register(JobMatch)
class JobMatchAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "resume",
        "match_score",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "resume__full_name",
        "resume__email",
        "resume__user__email",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )