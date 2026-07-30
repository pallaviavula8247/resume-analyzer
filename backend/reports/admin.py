from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """
    Admin configuration for Report model.
    """

    list_display = (
        "id",
        "report_title",
        "resume",
        "ats_score",
        "match_score",
        "status",
        "generated_at",
    )

    list_filter = (
        "status",
        "generated_at",
    )

    search_fields = (
        "report_title",
        "resume__full_name",
        "resume__email",
        "resume__user__email",
    )

    ordering = (
        "-generated_at",
    )

    readonly_fields = (
        "generated_at",
        "updated_at",
    )