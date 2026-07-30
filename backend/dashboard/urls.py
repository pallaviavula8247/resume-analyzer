from django.urls import path

from .views import (
    DashboardView,
    ResumeHistoryView,
    ResumeDetailView,
    DeleteResumeView,
)

urlpatterns = [

    path(
        "",
        DashboardView.as_view(),
        name="dashboard",
    ),

    path(
        "history/",
        ResumeHistoryView.as_view(),
        name="history",
    ),

    path(
        "resume/<int:resume_id>/",
        ResumeDetailView.as_view(),
        name="resume-detail",
    ),

    path(
        "resume/<int:resume_id>/delete/",
        DeleteResumeView.as_view(),
        name="resume-delete",
    ),
]