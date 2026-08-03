from django.urls import path

from .views import (
    AnalyzeResumeView,
    JobMatchView,
)

urlpatterns = [

    # ==========================
    # ATS Analysis
    # ==========================
    path(
        "analyze/<int:resume_id>/",
        AnalyzeResumeView.as_view(),
        name="analyze_resume",
    ),

    # ==========================
    # Job Matching
    # ==========================
    path(
        "match/<int:resume_id>/",
        JobMatchView.as_view(),
        name="job_match",
    ),

]