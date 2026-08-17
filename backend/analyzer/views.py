from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume
from analyzer.models import ATSAnalysis

from .services.ats import analyze_resume
from .services.job_match import generate_job_matches


# ============================================================
# ATS ANALYSIS
# ============================================================

class AnalyzeResumeView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        resume_id
    ):

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
        # RUN ANALYSIS
        # ----------------------------------------------------

        try:

            analysis_data = analyze_resume(
                resume
            )

        except Exception as error:

            print(
                "ATS ANALYSIS ERROR:",
                error
            )

            return Response(
                {
                    "success": False,
                    "message": "Unable to analyze resume.",
                    "error": str(error)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


        # ----------------------------------------------------
        # SAVE / UPDATE ANALYSIS
        # ----------------------------------------------------

        ats_analysis, created = ATSAnalysis.objects.update_or_create(

            resume=resume,

            defaults=analysis_data
        )


        return Response(
            {
                "success": True,

                "message":
                    "Resume analyzed successfully.",

                "data": {

                    "id":
                        ats_analysis.id,

                    "resume_id":
                        resume.id,

                    "ats_score":
                        ats_analysis.ats_score,

                    "keyword_score":
                        ats_analysis.keyword_score,

                    "skill_score":
                        ats_analysis.skill_score,

                    "education_score":
                        ats_analysis.education_score,

                    "experience_score":
                        ats_analysis.experience_score,

                    "project_score":
                        ats_analysis.project_score,

                    "certification_score":
                        ats_analysis.certification_score,

                    "format_score":
                        ats_analysis.format_score,

                    "strengths":
                        ats_analysis.strengths,

                    "weaknesses":
                        ats_analysis.weaknesses,

                    "missing_skills":
                        ats_analysis.missing_skills,

                    "recommendations":
                        ats_analysis.recommendations,

                }
            },

            status=status.HTTP_200_OK
        )


# ============================================================
# JOB MATCH
# ============================================================

class JobMatchView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        resume_id
    ):

        # ----------------------------------------------------
        # GET RESUME
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
        # GENERATE JOB MATCHES
        # ----------------------------------------------------

        try:

            jobs = generate_job_matches(
                resume
            )

        except Exception as error:

            print(
                "JOB MATCH ERROR:",
                error
            )

            return Response(
                {
                    "success": False,
                    "message":
                        "Unable to generate job matches.",
                    "error":
                        str(error)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


        # ----------------------------------------------------
        # GET ATS SCORE
        # ----------------------------------------------------

        ats_score = 0

        try:

            ats_analysis = ATSAnalysis.objects.filter(
                resume=resume
            ).first()

            if ats_analysis:

                ats_score = (
                    ats_analysis.ats_score
                    or 0
                )

        except Exception:

            ats_score = 0


        # ----------------------------------------------------
        # RESPONSE
        # ----------------------------------------------------

        return Response(
            {
                "success": True,

                "message":
                    "Job matches generated successfully.",

                "data": {

                    "resume_id":
                        resume.id,

                    "resume_score":
                        ats_score,

                    "ats_score":
                        ats_score,

                    "total_jobs":
                        len(jobs),

                    "best_match":
                        jobs[0]["title"]
                        if jobs
                        else None,

                    "jobs":
                        jobs,

                    "matches":
                        jobs,

                    "job_matches":
                        jobs,

                }
            },

            status=status.HTTP_200_OK
        )