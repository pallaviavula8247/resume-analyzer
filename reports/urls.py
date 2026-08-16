from django.urls import path

from .views import (
    ReportListView,
    GenerateReportView,
    ReportDetailView,
    DeleteReportView,
    DownloadReportView,
)

urlpatterns = [

    # GET - report history
    path(
        "",
        ReportListView.as_view(),
        name="report-list",
    ),

    # POST - generate report
    path(
        "generate/<int:resume_id>/",
        GenerateReportView.as_view(),
        name="generate-report",
    ),

    # GET - single report
    path(
        "<int:report_id>/",
        ReportDetailView.as_view(),
        name="report-detail",
    ),

    # DELETE
    path(
        "<int:report_id>/delete/",
        DeleteReportView.as_view(),
        name="delete-report",
    ),

    # GET - download
    path(
        "<int:report_id>/download/",
        DownloadReportView.as_view(),
        name="download-report",
    ),

]