"""
reports/views.py

API views for Resume Analyzer Reports.
"""

import os

from django.conf import settings
from django.core.files import File
from django.http import FileResponse

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from parser.models import Resume

from .models import Report
from .serializers import ReportSerializer

from .services.report_builder import build_report
from .services.pdf_generator import generate_pdf


# ============================================================
# HELPER - GENERATE PDF
# ============================================================

def generate_report_pdf(resume_id):
    """
    Build report data and generate PDF.
    """

    report_data = build_report(resume_id)

    if not report_data:
        return None, None

    reports_dir = os.path.join(
        settings.MEDIA_ROOT,
        "reports"
    )

    os.makedirs(
        reports_dir,
        exist_ok=True
    )

    pdf_path = os.path.join(
        reports_dir,
        f"report_{resume_id}.pdf"
    )

    try:
        generate_pdf(
            report_data,
            pdf_path
        )

    except Exception as e:

        print(
            "PDF GENERATION ERROR:",
            e
        )

        return report_data, None

    if not os.path.exists(pdf_path):
        return report_data, None

    return report_data, pdf_path


# ============================================================
# 1. GENERATE REPORT
# ============================================================

class ReportGenerateView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        resume_id
    ):

        # ----------------------------------------------------
        # Check resume
        # ----------------------------------------------------

        try:

            resume = Resume.objects.get(
                id=resume_id,
                user=request.user
            )

        except Resume.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Resume not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------------------------
        # Generate PDF
        # ----------------------------------------------------

        report_data, pdf_path = generate_report_pdf(
            resume_id
        )

        if not report_data:

            return Response(
                {
                    "success": False,
                    "message": "Unable to build report."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not pdf_path:

            return Response(
                {
                    "success": False,
                    "message": "Unable to generate PDF."
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # ----------------------------------------------------
        # Summary
        # ----------------------------------------------------

        summary = report_data.get(
            "summary",
            {}
        )

        ats_score = summary.get(
            "ats_score",
            0
        )

        # ----------------------------------------------------
        # Job match score
        # ----------------------------------------------------

        job_matches = report_data.get(
            "job_matches",
            []
        )

        match_score = 0

        if job_matches:

            match_score = job_matches[0].get(
                "match_score",
                0
            )

        # ----------------------------------------------------
        # Report information
        # ----------------------------------------------------

        report_info = report_data.get(
            "report_info",
            {}
        )

        candidate = report_data.get(
            "candidate",
            {}
        )

        recommendations = report_data.get(
            "recommendations",
            []
        )

        # ----------------------------------------------------
        # Save database report
        # ----------------------------------------------------

        report = Report.objects.create(

            resume=resume,

            report_title=report_info.get(
                "title",
                "AI Resume Analyzer Report"
            ),

            report_version=report_info.get(
                "version",
                "1.0"
            ),

            ats_score=ats_score,

            match_score=match_score,

            parsed_data=candidate,

            recommendations=recommendations,

            status="Generated"
        )

        # ----------------------------------------------------
        # Save PDF
        # ----------------------------------------------------

        try:

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                report.pdf_file.save(
                    f"report_{resume_id}.pdf",
                    File(pdf_file),
                    save=True
                )

        except Exception as e:

            print(
                "PDF SAVE ERROR:",
                e
            )

            report.status = "Failed"

            report.save(
                update_fields=[
                    "status"
                ]
            )

            return Response(
                {
                    "success": False,
                    "message": "Failed to save PDF.",
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # ----------------------------------------------------
        # PDF URL
        # ----------------------------------------------------

        pdf_url = request.build_absolute_uri(
            report.pdf_file.url
        )

        # ----------------------------------------------------
        # Serialize
        # ----------------------------------------------------

        serializer = ReportSerializer(
            report
        )

        # ----------------------------------------------------
        # Response
        # ----------------------------------------------------

        return Response(
            {
                "success": True,
                "message": "Report generated successfully.",

                "report_id": report.id,

                "resume_id": resume_id,

                "pdf_url": pdf_url,

                "report": report_data,

                "database_report": serializer.data
            },
            status=status.HTTP_200_OK
        )


# ============================================================
# 2. REPORT LIST
# ============================================================

class ReportListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        reports = Report.objects.filter(
            resume__user=request.user
        ).order_by(
            "-generated_at"
        )

        serializer = ReportSerializer(
            reports,
            many=True
        )

        return Response(
            {
                "success": True,
                "count": reports.count(),
                "reports": serializer.data
            },
            status=status.HTTP_200_OK
        )


# ============================================================
# 3. REPORT HISTORY
# ============================================================

class ReportHistoryView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        reports = Report.objects.filter(
            resume__user=request.user
        ).order_by(
            "-generated_at"
        )

        serializer = ReportSerializer(
            reports,
            many=True
        )

        return Response(
            {
                "success": True,
                "count": reports.count(),
                "history": serializer.data
            },
            status=status.HTTP_200_OK
        )


# ============================================================
# 4. REPORT DETAIL
# ============================================================

class ReportDetailView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        report_id
    ):

        try:

            report = Report.objects.get(
                id=report_id,
                resume__user=request.user
            )

        except Report.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Report not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReportSerializer(
            report
        )

        return Response(
            {
                "success": True,
                "report": serializer.data
            },
            status=status.HTTP_200_OK
        )


# ============================================================
# 5. DOWNLOAD PDF
# ============================================================

class ReportPDFView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        resume_id
    ):

        # ----------------------------------------------------
        # Check resume
        # ----------------------------------------------------

        try:

            Resume.objects.get(
                id=resume_id,
                user=request.user
            )

        except Resume.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Resume not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------------------------
        # Generate PDF
        # ----------------------------------------------------

        report_data, pdf_path = generate_report_pdf(
            resume_id
        )

        if not pdf_path:

            return Response(
                {
                    "success": False,
                    "message": "PDF could not be generated."
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # ----------------------------------------------------
        # Download
        # ----------------------------------------------------

        return FileResponse(
            open(
                pdf_path,
                "rb"
            ),
            as_attachment=True,
            filename=f"resume_report_{resume_id}.pdf",
            content_type="application/pdf"
        )


# ============================================================
# 6. DELETE REPORT
# ============================================================

class ReportDeleteView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        report_id
    ):

        try:

            report = Report.objects.get(
                id=report_id,
                resume__user=request.user
            )

        except Report.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Report not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ----------------------------------------------------
        # Delete PDF file
        # ----------------------------------------------------

        try:

            if report.pdf_file:

                pdf_path = report.pdf_file.path

                if os.path.exists(pdf_path):

                    os.remove(
                        pdf_path
                    )

        except Exception as e:

            print(
                "PDF DELETE WARNING:",
                e
            )

        # ----------------------------------------------------
        # Delete database record
        # ----------------------------------------------------

        report.delete()

        return Response(
            {
                "success": True,
                "message": "Report deleted successfully."
            },
            status=status.HTTP_200_OK
        )