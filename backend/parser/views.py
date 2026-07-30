from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import ResumeUploadSerializer
from .utils import extract_text
from .services import parse_resume


class ResumeUploadView(APIView):
    """
    Resume Upload API
    """

    permission_classes = [IsAuthenticated]

    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def post(self, request):

        serializer = ResumeUploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Save uploaded resume
        resume = serializer.save(user=request.user)

        # Extract resume text
        text = extract_text(resume.resume_file.path)

        # Parse resume
        parsed_data = parse_resume(text)

        # Save extracted information
        resume.extracted_text = text

        resume.full_name = parsed_data.get("full_name", "")
        resume.email = parsed_data.get("email", "")
        resume.phone = parsed_data.get("phone", "")
        resume.location = parsed_data.get("location", "")

        resume.linkedin = parsed_data.get("linkedin", "")
        resume.github = parsed_data.get("github", "")
        resume.portfolio = parsed_data.get("portfolio", "")

        resume.skills = parsed_data.get("skills", [])
        resume.education = parsed_data.get("education", [])
        resume.experience = parsed_data.get("experience", [])
        resume.projects = parsed_data.get("projects", [])
        resume.certifications = parsed_data.get("certifications", [])
        resume.languages = parsed_data.get("languages", [])

        resume.ats_score = parsed_data.get("ats_score", 0)
        resume.missing_skills = parsed_data.get("missing_skills", [])

        # IMPORTANT
        resume.ai_recommendations = parsed_data.get(
            "recommendations",
            [],
        )

        resume.save()

        return Response(
            {
                "message": "Resume uploaded successfully.",
                "resume_id": resume.id,
                "parsed_data": parsed_data,
            },
            status=status.HTTP_201_CREATED,
        )