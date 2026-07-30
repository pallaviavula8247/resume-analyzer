from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume

from .models import Report
from .serializers import ReportSerializer
from .services import build_report
from .pdf_generator import generate_report_pdf


class GenerateReportView(APIView):
    """
    Generate AI Resume Analysis Report
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, resume_id):

        resume = get_object_or_404(
            Resume,
            id=resume_id,
            user=request.user,
        )

        # Build report
        report = build_report(resume)

        # Generate PDF
        generate_report_pdf(report)

        # Update status
        report.status = "Generated"
        report.save()

        serializer = ReportSerializer(report)

        return Response(
            {
                "message": "Report generated successfully.",
                "report": serializer.data,
                "pdf_url": report.pdf_file.url if report.pdf_file else None,
            },
            status=status.HTTP_201_CREATED,
        )


class ReportHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        reports = Report.objects.filter(
            resume__user=request.user
        )

        serializer = ReportSerializer(
            reports,
            many=True,
        )

        return Response(serializer.data)


class ReportDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, report_id):

        report = get_object_or_404(
            Report,
            id=report_id,
            resume__user=request.user,
        )

        serializer = ReportSerializer(report)

        return Response(serializer.data)


class DeleteReportView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, report_id):

        report = get_object_or_404(
            Report,
            id=report_id,
            resume__user=request.user,
        )

        report.delete()

        return Response(
            {
                "message": "Report deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT,
        )


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
                    "error": "PDF not generated yet."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        report.status = "Downloaded"
        report.save()

        return Response(
            {
                "message": "PDF ready.",
                "pdf_url": report.pdf_file.url,
            }
        )