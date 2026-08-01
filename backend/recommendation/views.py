from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume
from analyzer.models import ATSAnalysis

from .services.recommender import generate_recommendations
from .serializers import RecommendationSerializer


class RecommendationView(APIView):
    """
    Generate AI recommendations for a resume.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, resume_id):

        # -----------------------------
        # Get Resume
        # -----------------------------
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

        # -----------------------------
        # Get ATS Analysis
        # -----------------------------
        try:
            ats_analysis = ATSAnalysis.objects.get(
                resume=resume
            )

        except ATSAnalysis.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": (
                        "ATS analysis not found. "
                        "Please analyze the resume first."
                    ),
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # -----------------------------
        # Generate Recommendations
        # -----------------------------
        recommendations = generate_recommendations(
            resume,
            ats_analysis,
        )

        serializer = RecommendationSerializer(
            recommendations
        )

        # -----------------------------
        # Response
        # -----------------------------
        return Response(
            {
                "success": True,
                "message": "Recommendations generated successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )