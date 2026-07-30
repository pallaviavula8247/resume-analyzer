from rest_framework import serializers

from parser.models import Resume


class ResumeHistorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Resume

        fields = [
            "id",
            "resume_file",
            "uploaded_at",
        ]