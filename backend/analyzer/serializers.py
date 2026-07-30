from rest_framework import serializers


class JobDescriptionSerializer(serializers.Serializer):
    job_description = serializers.CharField(
        required=True
    )