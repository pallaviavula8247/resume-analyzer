"""
dashboard/views.py

Dashboard APIs for Resume Analyzer.
"""

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .services.dashboard import get_dashboard_data
from .services.history import get_resume_history
from .services.detail import get_resume_detail
from .services.delete import delete_resume

from .serializers import DashboardSerializer


class DashboardView(APIView):
    """
    GET /api/dashboard/

    Returns complete dashboard data for the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:

            dashboard_data = get_dashboard_data(request.user)

            serializer = DashboardSerializer(
                dashboard_data
            )

            return Response(
                {
                    "success": True,
                    "message": "Dashboard loaded successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ResumeHistoryView(APIView):
    """
    GET /api/dashboard/history/
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:

            history = get_resume_history(request.user)

            return Response(
                {
                    "success": True,
                    "count": len(history),
                    "data": history,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ResumeDetailView(APIView):
    """
    GET /api/dashboard/resume/<resume_id>/
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

        try:

            resume = get_resume_detail(
                request.user,
                resume_id,
            )

            if resume is None:

                return Response(
                    {
                        "success": False,
                        "message": "Resume not found.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            return Response(
                {
                    "success": True,
                    "data": resume,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class DeleteResumeView(APIView):
    """
    DELETE /api/dashboard/resume/<resume_id>/delete/
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, resume_id):

        try:

            deleted = delete_resume(
                request.user,
                resume_id,
            )

            if not deleted:

                return Response(
                    {
                        "success": False,
                        "message": "Resume not found.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            return Response(
                {
                    "success": True,
                    "message": "Resume deleted successfully.",
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )