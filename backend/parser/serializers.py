"""
parser/serializers.py

Serializers for Resume Upload and Resume Details
"""

from rest_framework import serializers
from .models import Resume


# ======================================================
# Resume Upload Serializer
# ======================================================
class ResumeUploadSerializer(serializers.ModelSerializer):
    """
    Serializer used for uploading a resume.
    """

    class Meta:
        model = Resume

        fields = (
            "id",
            "resume_file",
            "uploaded_at",
        )

        read_only_fields = (
            "id",
            "uploaded_at",
        )


# ======================================================
# Resume Detail Serializer
# ======================================================
class ResumeSerializer(serializers.ModelSerializer):
    """
    Serializer used for listing and viewing parsed resumes.
    """

    class Meta:
        model = Resume

        fields = (
            "id",
            "user",
            "resume_file",
            "uploaded_at",
            "extracted_text",
            "full_name",
            "email",
            "phone",
            "location",
            "linkedin",
            "github",
            "portfolio",
            "skills",
            "education",
            "experience",
            "projects",
            "certifications",
            "languages",
            "ats_score",
            "missing_skills",
            "ai_recommendations",
        )

        read_only_fields = (
            "id",
            "user",
            "uploaded_at",
            "extracted_text",
            "full_name",
            "email",
            "phone",
            "location",
            "linkedin",
            "github",
            "portfolio",
            "skills",
            "education",
            "experience",
            "projects",
            "certifications",
            "languages",
            "ats_score",
            "missing_skills",
            "ai_recommendations",
        )