from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume
from parser.services import parse_resume

from .serializers import ResumeHistorySerializer
from .services import get_dashboard_data


class DashboardView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        data = get_dashboard_data(
            request.user
        )

        return Response(
            {
                "success": True,
                "dashboard": data,
            },
            status=status.HTTP_200_OK,
        )


class ResumeHistoryView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        resumes = Resume.objects.filter(
            user=request.user
        ).order_by("-uploaded_at")

        serializer = ResumeHistorySerializer(
            resumes,
            many=True,
        )

        return Response(
            serializer.data
        )


class ResumeDetailView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        resume_id,
    ):

        try:

            resume = Resume.objects.get(
                id=resume_id,
                user=request.user,
            )

        except Resume.DoesNotExist:

            return Response(
                {
                    "error": "Resume not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        parsed = parse_resume(
            resume.extracted_text
        )

        return Response(
            parsed
        )


class DeleteResumeView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        resume_id,
    ):

        try:

            resume = Resume.objects.get(
                id=resume_id,
                user=request.user,
            )

        except Resume.DoesNotExist:

            return Response(
                {
                    "error": "Resume not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        resume.delete()

        return Response(
            {
                "success": True,
                "message": "Resume deleted successfully."
            }
        )