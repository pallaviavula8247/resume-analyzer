from django.urls import path

from .views import (
    AnalyzeResumeView,
    JobMatchView,
)

urlpatterns = [

    path(
        "analyze/<int:resume_id>/",
        AnalyzeResumeView.as_view(),
        name="analyze_resume",
    ),

    path(
        "match/<int:resume_id>/",
        JobMatchView.as_view(),
        name="job_match",
    ),

]