from django.urls import path

from .views import (
    ReportGenerateView,
    ReportListView,
    ReportHistoryView,
    ReportDetailView,
    ReportPDFView,
    ReportDeleteView,
)


urlpatterns = [

    # Generate report
    path(
        "generate/<int:resume_id>/",
        ReportGenerateView.as_view(),
        name="generate-report"
    ),

    # Report list
    path(
        "",
        ReportListView.as_view(),
        name="report-list"
    ),

    # Report history
    path(
        "history/",
        ReportHistoryView.as_view(),
        name="report-history"
    ),

    # Report detail
    path(
        "<int:report_id>/",
        ReportDetailView.as_view(),
        name="report-detail"
    ),

    # Download PDF
    path(
        "<int:resume_id>/pdf/",
        ReportPDFView.as_view(),
        name="report-pdf"
    ),

    # Delete report
    path(
        "<int:report_id>/delete/",
        ReportDeleteView.as_view(),
        name="report-delete"
    ),

]