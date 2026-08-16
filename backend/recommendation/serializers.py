from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )

    platform = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )

    level = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )

    difficulty = serializers.CharField(
        required=False,
        allow_blank=True,
        default=""
    )

    technologies = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        default=list
    )


class RecommendationSerializer(serializers.Serializer):
    """
    Serializer for AI-generated resume recommendations.
    """

    # ---------------------------------------------------------
    # Basic information
    # ---------------------------------------------------------

    id = serializers.IntegerField(
        required=False
    )

    resume_id = serializers.IntegerField(
        required=False
    )

    created = serializers.BooleanField(
        required=False
    )

    # ---------------------------------------------------------
    # Career recommendations
    # ---------------------------------------------------------

    recommended_roles = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        default=list
    )

    # ---------------------------------------------------------
    # Skill recommendations
    # ---------------------------------------------------------

    recommended_skills = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        default=list
    )

    # ---------------------------------------------------------
    # Course recommendations
    # ---------------------------------------------------------

    recommended_courses = CourseSerializer(
        many=True,
        required=False,
        default=list
    )

    # ---------------------------------------------------------
    # Project recommendations
    # ---------------------------------------------------------

    recommended_projects = ProjectSerializer(
        many=True,
        required=False,
        default=list
    )

    # ---------------------------------------------------------
    # Learning roadmap
    # ---------------------------------------------------------

    learning_roadmap = serializers.DictField(
        required=False,
        default=dict
    )

    # ---------------------------------------------------------
    # Resume improvement tips
    # ---------------------------------------------------------

    resume_tips = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        default=list
    )