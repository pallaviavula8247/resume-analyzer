from django.urls import path

from .views import (
    GenerateReportView,
    ReportHistoryView,
    ReportDetailView,
    DeleteReportView,
    DownloadReportView,
    ResumeReportPDFView,
)


urlpatterns = [

    # Generate report
    path(
        "generate/<int:resume_id>/",
        GenerateReportView.as_view(),
        name="generate-report",
    ),


    # Report history
    path(
        "",
        ReportHistoryView.as_view(),
        name="report-history",
    ),


    # Report detail
    path(
        "<int:report_id>/",
        ReportDetailView.as_view(),
        name="report-detail",
    ),


    # Delete report
    path(
        "<int:report_id>/delete/",
        DeleteReportView.as_view(),
        name="delete-report",
    ),


    # Download saved report
    path(
        "<int:report_id>/download/",
        DownloadReportView.as_view(),
        name="download-report",
    ),


    # Generate AI Resume Analyzer PDF directly
    path(
        "<int:resume_id>/pdf/",
        ResumeReportPDFView.as_view(),
        name="resume-report-pdf",
    ),

]