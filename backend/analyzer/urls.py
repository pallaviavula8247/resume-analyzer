from django.urls import path

from .views import (
    AnalyzeResumeView,
    JobMatchView,
)


# ============================================================
# ANALYZER URLS
# ============================================================

urlpatterns = [

    # ========================================================
    # ATS RESUME ANALYSIS
    # ========================================================

    path(
        "analyze/<int:resume_id>/",
        AnalyzeResumeView.as_view(),
        name="analyze-resume",
    ),


    # ========================================================
    # JOB MATCH
    # ========================================================

    path(
        "match/<int:resume_id>/",
        JobMatchView.as_view(),
        name="job-match",
    ),

]

