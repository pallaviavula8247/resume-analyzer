from rest_framework import serializers

from .models import ATSAnalysis, JobMatch


class ATSAnalysisSerializer(serializers.ModelSerializer):
    """
    Serializer for ATS Analysis.
    """

    class Meta:
        model = ATSAnalysis
        fields = "__all__"
        read_only_fields = (
            "resume",
            "analyzed_at",
            "updated_at",
        )


class JobMatchSerializer(serializers.ModelSerializer):
    """
    Serializer for Job Match.
    """

    class Meta:
        model = JobMatch
        fields = "__all__"
        read_only_fields = (
            "resume",
            "match_score",
            "match_level",
            "matched_skills",
            "missing_skills",
            "extra_skills",
            "recommendations",
            "created_at",
            "updated_at",
        )


class JobDescriptionSerializer(serializers.Serializer):
    """
    Input serializer for Job Matching.
    """

    job_title = serializers.CharField(
        max_length=255,
        required=False,
        allow_blank=True,
    )

    job_description = serializers.CharField(
        required=True,
        allow_blank=False,
    )