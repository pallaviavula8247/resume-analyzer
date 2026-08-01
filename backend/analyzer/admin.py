from django.contrib import admin
from .models import ATSAnalysis


@admin.register(ATSAnalysis)
class ATSAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "ats_score",
        "keyword_score",
        "skill_score",
        "analyzed_at",
    )

    search_fields = (
        "resume__full_name",
        "resume__email",
    )

    list_filter = (
        "ats_score",
        "analyzed_at",
    )