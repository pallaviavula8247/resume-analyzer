"""
dashboard/serializers.py

Serializers for Dashboard APIs.
"""

from rest_framework import serializers


# ==========================================
# User
# ==========================================

class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    full_name = serializers.CharField()

    email = serializers.EmailField()


# ==========================================
# Statistics
# ==========================================

class StatisticsSerializer(serializers.Serializer):

    total_resumes = serializers.IntegerField()

    average_ats_score = serializers.FloatField()

    highest_ats_score = serializers.IntegerField()

    total_job_matches = serializers.IntegerField()

    total_recommendations = serializers.IntegerField()


# ==========================================
# ATS Chart
# ==========================================

class ATSChartSerializer(serializers.Serializer):

    labels = serializers.ListField(
        child=serializers.CharField()
    )

    scores = serializers.ListField(
        child=serializers.IntegerField()
    )


# ==========================================
# Job Match Chart
# ==========================================

class JobMatchChartSerializer(serializers.Serializer):

    labels = serializers.ListField(
        child=serializers.CharField()
    )

    scores = serializers.ListField(
        child=serializers.IntegerField()
    )


# ==========================================
# Skills Chart
# ==========================================

class SkillsChartSerializer(serializers.Serializer):

    labels = serializers.ListField(
        child=serializers.CharField()
    )

    counts = serializers.ListField(
        child=serializers.IntegerField()
    )


# ==========================================
# Timeline Chart
# ==========================================

class TimelineChartSerializer(serializers.Serializer):

    labels = serializers.ListField(
        child=serializers.CharField()
    )

    uploads = serializers.ListField(
        child=serializers.IntegerField()
    )


# ==========================================
# Charts
# ==========================================

class ChartsSerializer(serializers.Serializer):

    ats_chart = ATSChartSerializer()

    job_match_chart = JobMatchChartSerializer()

    skills_chart = SkillsChartSerializer()

    timeline_chart = TimelineChartSerializer()


# ==========================================
# Latest Resume
# ==========================================

class LatestResumeSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    full_name = serializers.CharField()

    email = serializers.EmailField(
        allow_blank=True,
        required=False,
    )

    phone = serializers.CharField(
        allow_blank=True,
        required=False,
    )

    uploaded_at = serializers.DateTimeField()


# ==========================================
# ATS Analysis
# ==========================================

class ATSSerializer(serializers.Serializer):

    ats_score = serializers.IntegerField()

    keyword_score = serializers.IntegerField()

    skill_score = serializers.IntegerField()

    education_score = serializers.IntegerField()

    experience_score = serializers.IntegerField()

    project_score = serializers.IntegerField()

    certification_score = serializers.IntegerField()

    format_score = serializers.IntegerField()

    strengths = serializers.ListField(
        child=serializers.CharField()
    )

    weaknesses = serializers.ListField(
        child=serializers.CharField()
    )

    missing_skills = serializers.ListField(
        child=serializers.CharField()
    )


# ==========================================
# Job Match
# ==========================================

class JobMatchSerializer(serializers.Serializer):

    job_title = serializers.CharField()

    match_score = serializers.IntegerField()

    match_level = serializers.CharField()


# ==========================================
# Recommendation
# ==========================================

class RecommendationSerializer(serializers.Serializer):

    title = serializers.CharField()

    description = serializers.CharField()


# ==========================================
# Dashboard
# ==========================================

class DashboardSerializer(serializers.Serializer):

    user = UserSerializer()

    statistics = StatisticsSerializer()

    charts = ChartsSerializer()

    latest_resume_id = serializers.IntegerField(
        allow_null=True
    )

    latest_resume = LatestResumeSerializer(
        allow_null=True
    )

    ats = ATSSerializer(
        allow_null=True
    )

    job_matches = JobMatchSerializer(
        many=True
    )

    recommendations = RecommendationSerializer(
        many=True
    )

    recent_activity = serializers.ListField(
        child=serializers.CharField()
    )