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
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

        data = get_dashboard_data(request.user)

        serializer = DashboardSerializer(data)

        return Response(
            {
                "success": True,
                "message": "Dashboard data retrieved successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class ResumeHistoryView(APIView):
    """
    GET /api/dashboard/history/
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

        history = get_resume_history(request.user)

        return Response(
            {
                "success": True,
                "count": len(history),
                "data": history,
            },
            status=status.HTTP_200_OK,
        )


class ResumeDetailView(APIView):
    """
    GET /api/dashboard/resume/<resume_id>/
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

        data = get_resume_detail(
            request.user,
            resume_id,
        )

        if data is None:

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
                "data": data,
            },
            status=status.HTTP_200_OK,
        )


class DeleteResumeView(APIView):
    """
    DELETE /api/dashboard/resume/<resume_id>/delete/
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, resume_id):

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