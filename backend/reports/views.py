"""
reports/views.py

API views for report management and PDF generation.
"""

import os

from django.conf import settings
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.core.files import File

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume

from .models import Report
from .serializers import ReportSerializer
from .services.report_builder import build_report
from .services.pdf_generator import generate_pdf


# ==================================
# Generate Report
# ==================================

class GenerateReportView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, resume_id):

        try:
            resume = Resume.objects.get(
                id=resume_id,
                user=request.user,
            )

        except Resume.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Resume not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        report_data = build_report(resume_id)

        if not report_data:

            return Response(
                {
                    "success": False,
                    "message": "Unable to generate report.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        ats_score = 0
        match_score = 0

        if report_data.get("ats_analysis"):
            ats_score = report_data["ats_analysis"].get(
                "ats_score",
                0,
            )

        if report_data.get("job_matches"):

            match_score = report_data["job_matches"][0].get(
                "match_score",
                0,
            )

        report = Report.objects.create(
            resume=resume,
            report_title=f"{resume.full_name} Resume Report",
            ats_score=ats_score,
            match_score=match_score,
            parsed_data=report_data,
            recommendations=report_data.get(
                "recommendations",
                [],
            ),
            status="Generated",
        )

        reports_folder = os.path.join(
            settings.MEDIA_ROOT,
            "reports",
        )

        os.makedirs(
            reports_folder,
            exist_ok=True,
        )

        pdf_path = os.path.join(
            reports_folder,
            f"report_{report.id}.pdf",
        )

        generate_pdf(
            report_data,
            pdf_path,
        )

        with open(pdf_path, "rb") as pdf:

            report.pdf_file.save(
                f"report_{report.id}.pdf",
                File(pdf),
                save=True,
            )

        serializer = ReportSerializer(report)

        return Response(
            {
                "success": True,
                "message": "Report generated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


# ==================================
# Report History
# ==================================

class ReportHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        reports = Report.objects.filter(
            resume__user=request.user
        ).order_by("-generated_at")

        serializer = ReportSerializer(
            reports,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": reports.count(),
                "data": serializer.data,
            }
        )


# ==================================
# Report Detail
# ==================================

class ReportDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, report_id):

        report = get_object_or_404(
            Report,
            id=report_id,
            resume__user=request.user,
        )

        serializer = ReportSerializer(report)

        return Response(
            {
                "success": True,
                "data": serializer.data,
            }
        )


# ==================================
# Delete Report
# ==================================

class DeleteReportView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, report_id):

        report = get_object_or_404(
            Report,
            id=report_id,
            resume__user=request.user,
        )

        if report.pdf_file:

            if os.path.exists(report.pdf_file.path):
                os.remove(report.pdf_file.path)

        report.delete()

        return Response(
            {
                "success": True,
                "message": "Report deleted successfully.",
            }
        )


# ==================================
# Download Saved Report
# ==================================

class DownloadReportView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, report_id):

        report = get_object_or_404(
            Report,
            id=report_id,
            resume__user=request.user,
        )

        if not report.pdf_file:

            return Response(
                {
                    "success": False,
                    "message": "PDF not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return FileResponse(
            report.pdf_file.open("rb"),
            as_attachment=True,
            filename=os.path.basename(
                report.pdf_file.name
            ),
        )


# ==================================
# Generate PDF Report Directly
# ==================================

class ResumeReportPDFView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

        try:

            report = build_report(resume_id)

            if not report:

                return Response(
                    {
                        "error": "Resume not found"
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            pdf_path = os.path.join(
                settings.BASE_DIR,
                "resume_analysis_report.pdf",
            )

            generate_pdf(
                report,
                pdf_path,
            )

            return FileResponse(
                open(pdf_path, "rb"),
                as_attachment=True,
                filename="AI_Resume_Analysis_Report.pdf",
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )