from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField()
    platform = serializers.CharField()
    level = serializers.CharField()


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField()
    difficulty = serializers.CharField()
    technologies = serializers.ListField(
        child=serializers.CharField()
    )


class RecommendationSerializer(serializers.Serializer):
    """
    Serializer for AI recommendation response.
    """

    recommended_careers = serializers.ListField(
        child=serializers.CharField()
    )

    recommended_courses = CourseSerializer(
        many=True
    )

    recommended_projects = ProjectSerializer(
        many=True
    )

    learning_roadmap = serializers.DictField(
        child=serializers.ListField(
            child=serializers.CharField()
        )
    )

    resume_tips = serializers.ListField(
        child=serializers.CharField()
    )