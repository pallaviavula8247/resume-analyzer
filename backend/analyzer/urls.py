from django.urls import path

from .views import AnalyzeResumeView

urlpatterns = [
    path(
        "analyze/<int:resume_id>/",
        AnalyzeResumeView.as_view(),
        name="analyze_resume",
    ),
]