from django.contrib import admin
from .models import ATSAnalysis, JobMatch


@admin.register(ATSAnalysis)
class ATSAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "ats_score",
        "keyword_score",
        "skill_score",
        "analyzed_at",
    )

    list_filter = (
        "analyzed_at",
    )


@admin.register(JobMatch)
class JobMatchAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "job_title",
        "match_score",
        "match_level",
        "created_at",
    )

    list_filter = (
        "created_at",
    )