from django.urls import path

from .views import (
    GenerateReportView,
    ReportHistoryView,
    ReportDetailView,
    DeleteReportView,
    DownloadReportView,
)

urlpatterns = [

    path(
        "generate/<int:resume_id>/",
        GenerateReportView.as_view(),
        name="generate-report",
    ),

    path(
        "",
        ReportHistoryView.as_view(),
        name="report-history",
    ),

    path(
        "<int:report_id>/",
        ReportDetailView.as_view(),
        name="report-detail",
    ),

    path(
        "<int:report_id>/delete/",
        DeleteReportView.as_view(),
        name="delete-report",
    ),

    path(
        "<int:report_id>/download/",
        DownloadReportView.as_view(),
        name="download-report",
    ),
]