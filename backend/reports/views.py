"""
reports/views.py

API views for Resume Analyzer Reports.
"""

import os

from django.conf import settings
from django.http import FileResponse
from django.core.files import File

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
# Helper Function
# ============================================================

def generate_report_pdf(resume_id):
    """
    Build report data and generate PDF.

    Returns:
        (report_data, pdf_path)
    """

    # --------------------------------------------------------
    # Build report
    # --------------------------------------------------------

    report_data = build_report(resume_id)

    if not report_data:
        return None, None

    # --------------------------------------------------------
    # Reports directory
    # --------------------------------------------------------

    reports_dir = os.path.join(
        settings.MEDIA_ROOT,
        "reports"
    )

    os.makedirs(
        reports_dir,
        exist_ok=True
    )

    # --------------------------------------------------------
    # PDF path
    # --------------------------------------------------------

    pdf_path = os.path.join(
        reports_dir,
        f"report_{resume_id}.pdf"
    )

    # --------------------------------------------------------
    # Generate PDF
    # --------------------------------------------------------

    try:

        generate_pdf(
            report_data,
            pdf_path
        )

    except Exception as e:

        print(
            f"PDF generation error: {e}"
        )

        return report_data, None

    # --------------------------------------------------------
    # Verify PDF
    # --------------------------------------------------------

    if not os.path.exists(pdf_path):

        return report_data, None

    return report_data, pdf_path


# ============================================================
# 1. Generate Report
# ============================================================

class ReportGenerateView(APIView):
    """
    Generate a PDF report for a resume.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

        # ----------------------------------------------------
        # Get Resume belonging to logged-in user
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
        # Build + Generate PDF
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
        # Extract summary values
        # ----------------------------------------------------

        summary = report_data.get(
            "summary",
            {}
        )

        ats_score = summary.get(
            "ats_score",
            0
        )

        job_matches = summary.get(
            "job_matches",
            0
        )

        # ----------------------------------------------------
        # Save report in database
        # ----------------------------------------------------

        report = Report.objects.create(

            resume=resume,

            report_title=report_data.get(
                "report_info",
                {}
            ).get(
                "title",
                "AI Resume Analyzer Report"
            ),

            report_version=report_data.get(
                "report_info",
                {}
            ).get(
                "version",
                "1.0"
            ),

            ats_score=ats_score,

            match_score=(
                report_data.get(
                    "job_matches",
                    [{}]
                )[0].get(
                    "match_score",
                    0
                )
                if report_data.get("job_matches")
                else 0
            ),

            parsed_data=report_data.get(
                "candidate",
                {}
            ),

            recommendations=report_data.get(
                "recommendations",
                []
            ),

            status="Generated"
        )

        # ----------------------------------------------------
        # Save PDF into FileField
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

            report.status = "Failed"
            report.save(
                update_fields=["status"]
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
        # Serialize report
        # ----------------------------------------------------

        serializer = ReportSerializer(
            report
        )

        # ----------------------------------------------------
        # Final response
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
# 2. Report List
# ============================================================

class ReportListView(APIView):
    """
    Return all reports belonging to the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

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
# 3. Report History
# ============================================================

class ReportHistoryView(APIView):
    """
    Return generated report history.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

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
# 4. Report Detail
# ============================================================

class ReportDetailView(APIView):
    """
    Get one report.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, report_id):

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
# 5. Download PDF
# ============================================================

class ReportPDFView(APIView):
    """
    Generate and download a PDF report.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

        # ----------------------------------------------------
        # Check Resume
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

        if not pdf_path:

            return Response(
                {
                    "success": False,
                    "message": "PDF could not be generated."
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # ----------------------------------------------------
        # Download PDF
        # ----------------------------------------------------

        return FileResponse(
            open(pdf_path, "rb"),
            as_attachment=True,
            filename=f"resume_report_{resume_id}.pdf",
            content_type="application/pdf"
        )


# ============================================================
# 6. Delete Report
# ============================================================

class ReportDeleteView(APIView):
    """
    Delete a report.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, report_id):

        # ----------------------------------------------------
        # Find report belonging to logged-in user
        # ----------------------------------------------------

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
        # Delete PDF
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
                f"PDF deletion warning: {e}"
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