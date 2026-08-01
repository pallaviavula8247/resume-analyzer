from rest_framework import serializers


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
# ATS Score Chart
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
# Recent Resume
# ==========================================

class RecentResumeSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    full_name = serializers.CharField()

    email = serializers.EmailField(
        allow_blank=True,
        required=False,
    )

    uploaded_at = serializers.DateTimeField()

    ats_score = serializers.IntegerField()


# ==========================================
# Dashboard Serializer
# ==========================================

class DashboardSerializer(serializers.Serializer):
    statistics = StatisticsSerializer()

    charts = ChartsSerializer()

    recent_resume = RecentResumeSerializer(
        allow_null=True
    )