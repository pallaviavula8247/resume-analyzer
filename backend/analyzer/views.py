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
    ATS Resume Analysis API.

    GET:
        Retrieve existing analysis.
        If analysis does not exist, generate it automatically.

    POST:
        Generate or regenerate ATS analysis.
    """

    permission_classes = [IsAuthenticated]

    # ==========================================================
    # GET ATS ANALYSIS
    # ==========================================================

    def get(self, request, resume_id):

        # ------------------------------------------------------
        # 1. Find Resume
        # ------------------------------------------------------

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
                    "resume_id": resume_id,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # ------------------------------------------------------
        # 2. Check Existing ATS Analysis
        # ------------------------------------------------------

        try:

            analysis = ATSAnalysis.objects.get(
                resume=resume,
            )

        except ATSAnalysis.DoesNotExist:

            # --------------------------------------------------
            # Generate Analysis Automatically
            # --------------------------------------------------

            try:

                result = analyze_resume(resume)

                analysis, created = (
                    ATSAnalysis.objects.update_or_create(
                        resume=resume,
                        defaults=result,
                    )
                )

            except Exception as error:

                return Response(
                    {
                        "success": False,
                        "message": "ATS analysis generation failed.",
                        "error": str(error),
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        # ------------------------------------------------------
        # 3. Serialize Analysis
        # ------------------------------------------------------

        serializer = ATSAnalysisSerializer(
            analysis
        )

        # ------------------------------------------------------
        # 4. Return Response
        # ------------------------------------------------------

        return Response(
            {
                "success": True,
                "message": "ATS analysis loaded successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # ==========================================================
    # POST ATS ANALYSIS
    # ==========================================================

    def post(self, request, resume_id):

        # ------------------------------------------------------
        # 1. Find Resume
        # ------------------------------------------------------

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
                    "resume_id": resume_id,
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # ------------------------------------------------------
        # 2. Generate ATS Analysis
        # ------------------------------------------------------

        try:

            result = analyze_resume(
                resume
            )

            # --------------------------------------------------
            # Save / Update Analysis
            # --------------------------------------------------

            analysis, created = (
                ATSAnalysis.objects.update_or_create(
                    resume=resume,
                    defaults=result,
                )
            )

            # --------------------------------------------------
            # Serialize
            # --------------------------------------------------

            serializer = ATSAnalysisSerializer(
                analysis
            )

            # --------------------------------------------------
            # Return
            # --------------------------------------------------

            return Response(
                {
                    "success": True,
                    "message": (
                        "ATS analysis generated successfully."
                    ),
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as error:

            return Response(
                {
                    "success": False,
                    "message": "ATS analysis failed.",
                    "error": str(error),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# =================================================================
# JOB MATCH
# =================================================================

class JobMatchView(APIView):
    """
    Job Matching API.

    GET:
        Retrieve previous job matches.

    POST:
        Generate a new job match.
    """

    permission_classes = [IsAuthenticated]

    # ==========================================================
    # GET JOB MATCHES
    # ==========================================================

    def get(self, request, resume_id):

        # ------------------------------------------------------
        # 1. Find Resume
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # 2. Get Matches
        # ------------------------------------------------------

        matches = (
            JobMatch.objects
            .filter(resume=resume)
            .order_by("-created_at")
        )

        # ------------------------------------------------------
        # 3. Serialize
        # ------------------------------------------------------

        serializer = JobMatchSerializer(
            matches,
            many=True,
        )

        # ------------------------------------------------------
        # 4. Return
        # ------------------------------------------------------

        return Response(
            {
                "success": True,
                "count": matches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # ==========================================================
    # POST JOB MATCH
    # ==========================================================

    def post(self, request, resume_id):

        # ------------------------------------------------------
        # 1. Validate Job Description
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # 2. Find Resume
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # 3. Generate Job Match
        # ------------------------------------------------------

        try:

            result = match_resume(
                {
                    "skills": resume.skills,
                },
                serializer.validated_data[
                    "job_description"
                ],
            )

            # --------------------------------------------------
            # 4. Save Job Match
            # --------------------------------------------------

            job_match = JobMatch.objects.create(

                resume=resume,

                job_title=(
                    serializer.validated_data.get(
                        "job_title",
                        "",
                    )
                ),

                job_description=(
                    serializer.validated_data[
                        "job_description"
                    ]
                ),

                match_score=int(
                    result.get(
                        "match_score",
                        0,
                    )
                ),

                match_level=result.get(
                    "match_level",
                    "",
                ),

                matched_skills=result.get(
                    "matched_skills",
                    [],
                ),

                missing_skills=result.get(
                    "missing_skills",
                    [],
                ),

                extra_skills=result.get(
                    "extra_skills",
                    [],
                ),

                recommendations=result.get(
                    "recommendations",
                    [],
                ),
            )

            # --------------------------------------------------
            # 5. Return
            # --------------------------------------------------

            return Response(
                {
                    "success": True,
                    "message": (
                        "Job matching completed successfully."
                    ),
                    "data": JobMatchSerializer(
                        job_match
                    ).data,
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as error:

            return Response(
                {
                    "success": False,
                    "message": "Job matching failed.",
                    "error": str(error),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )