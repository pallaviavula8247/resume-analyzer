from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume
from .models import ATSAnalysis, JobMatch
from .services.ats import analyze_resume
from .services.matcher import match_resume
from .serializers import (
    ATSAnalysisSerializer,
    JobDescriptionSerializer,
    JobMatchSerializer,
)


class AnalyzeResumeView(APIView):
    """
    POST -> Generate ATS Analysis
    GET  -> Retrieve Existing ATS Analysis
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

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
            analysis = ATSAnalysis.objects.get(
                resume=resume,
            )

        except ATSAnalysis.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "ATS Analysis not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ATSAnalysisSerializer(analysis)

        return Response(
            {
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

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

            serializer = ATSAnalysisSerializer(
                analysis
            )

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
                    "message": "ATS analysis failed.",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class JobMatchView(APIView):
    """
    POST -> Generate Job Match
    GET  -> Retrieve Job Matches
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

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

        matches = (
            JobMatch.objects.filter(
                resume=resume
            ).order_by("-created_at")
        )

        serializer = JobMatchSerializer(
            matches,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": matches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request, resume_id):

        serializer = JobDescriptionSerializer(
            data=request.data
        )

        if not serializer.is_valid():

            return Response(
                {
                    "success": False,
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

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

            result = match_resume(
                {
                    "skills": resume.skills,
                },
                serializer.validated_data[
                    "job_description"
                ],
            )

            job_match = JobMatch.objects.create(
                resume=resume,
                job_title=serializer.validated_data.get(
                    "job_title",
                    "",
                ),
                job_description=serializer.validated_data[
                    "job_description"
                ],
                match_score=int(
                    result["match_score"]
                ),
                match_level=result[
                    "match_level"
                ],
                matched_skills=result[
                    "matched_skills"
                ],
                missing_skills=result[
                    "missing_skills"
                ],
                extra_skills=result[
                    "extra_skills"
                ],
                recommendations=result[
                    "recommendations"
                ],
            )

            return Response(
                {
                    "success": True,
                    "message": "Job matching completed successfully.",
                    "data": JobMatchSerializer(
                        job_match
                    ).data,
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "message": "Job matching failed.",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )