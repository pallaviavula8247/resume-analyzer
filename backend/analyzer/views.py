from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume
from .models import JobMatch
from .matcher import match_resume
from .serializers import JobDescriptionSerializer


class JobMatchView(APIView):
    """
    Match uploaded resume with a job description.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, resume_id):

        serializer = JobDescriptionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
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

        # Run matching engine
        result = match_resume(
            {
                "skills": resume.skills
            },
            serializer.validated_data["job_description"],
        )

        # Save result into database
        job_match = JobMatch.objects.create(
            resume=resume,
            job_title="Software Engineer",
            job_description=serializer.validated_data["job_description"],

            # PositiveIntegerField requires integer
            match_score=int(result["match_score"]),

            matched_skills=result["matched_skills"],
            missing_skills=result["missing_skills"],

            recommendations=[
                f"Learn {skill}"
                for skill in result["missing_skills"]
            ],
        )

        return Response(
            {
                "success": True,
                "message": "Job matching completed successfully.",
                "job_match_id": job_match.id,
                "data": {
                    "match_score": round(result["match_score"], 2),
                    "match_level": result["match_level"],
                    "required_skills": result["required_skills"],
                    "matched_skills": result["matched_skills"],
                    "missing_skills": result["missing_skills"],
                    "extra_skills": result["extra_skills"],
                    "total_required_skills": result["total_required_skills"],
                    "matched_count": result["matched_count"],
                    "missing_count": result["missing_count"],
                    "extra_count": result["extra_count"],
                    "recommendations": [
                        f"Learn {skill}"
                        for skill in result["missing_skills"]
                    ],
                },
            },
            status=status.HTTP_200_OK,
        )