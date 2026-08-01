from rest_framework import serializers
from .models import ATSAnalysis


class ATSAnalysisSerializer(serializers.ModelSerializer):
    """
    Serializer for ATS Analysis results.
    """

    class Meta:
        model = ATSAnalysis

        fields = [
            "id",
            "resume",

            "ats_score",

            "keyword_score",
            "skill_score",
            "education_score",
            "experience_score",
            "project_score",
            "certification_score",
            "format_score",

            "strengths",
            "weaknesses",
            "missing_skills",
            "recommendations",

            "analyzed_at",
            "updated_at",
        ]

        read_only_fields = fields