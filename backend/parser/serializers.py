from rest_framework import serializers
from .models import Resume


class ResumeUploadSerializer(serializers.ModelSerializer):
    """
    Serializer for uploading and displaying resumes.
    """

    class Meta:
        model = Resume

        fields = [
            "id",
            "resume_file",
            "uploaded_at",
        ]

        read_only_fields = [
            "id",
            "uploaded_at",
        ]