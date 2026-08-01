from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume

from .models import ATSAnalysis
from .services.ats import analyze_resume
from .serializers import ATSAnalysisSerializer


class AnalyzeResumeView(APIView):

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

        try:

            result = analyze_resume(resume)

            analysis, created = ATSAnalysis.objects.update_or_create(
                resume=resume,
                defaults=result,
            )

            serializer = ATSAnalysisSerializer(analysis)

            return Response(
                {
                    "success": True,
                    "message": "ATS analysis completed successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )