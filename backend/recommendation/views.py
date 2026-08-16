from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from parser.models import Resume
from analyzer.models import ATSAnalysis

from .services.recommender import (
    generate_recommendations
)

from .serializers import (
    RecommendationSerializer
)


class RecommendationView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, resume_id):

        # ======================================================
        # GET RESUME
        # ======================================================

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

        # ======================================================
        # GET ATS ANALYSIS
        # ======================================================

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

        # ======================================================
        # GENERATE RECOMMENDATIONS
        # ======================================================

        try:

            recommendations = (
                generate_recommendations(
                    resume,
                    ats_analysis,
                )
            )

        except Exception as error:

            print(
                "Recommendation generation error:",
                error
            )

            return Response(
                {
                    "success": False,
                    "message": (
                        "Unable to generate recommendations."
                    ),
                    "error": str(error),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # ======================================================
        # SERIALIZE
        # ======================================================

        serializer = RecommendationSerializer(
            recommendations
        )

        # ======================================================
        # RESPONSE
        # ======================================================

        return Response(
            {
                "success": True,
                "message": (
                    "Recommendations generated successfully."
                ),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )