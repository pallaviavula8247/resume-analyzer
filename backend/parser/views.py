from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Resume
from .serializers import ResumeUploadSerializer
from .utils import extract_text
from .services import parse_resume


class ResumeUploadView(APIView):
    """
    Upload Resume, Extract Text and Parse Resume
    """

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = ResumeUploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Save uploaded resume
            resume = serializer.save(user=request.user)

            # Extract text
            text = extract_text(resume.resume_file.path)

            # Parse resume
            parsed_data = parse_resume(text)

            # Store extracted information
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

        except Exception as e:
            return Response(
                {
                    "message": "Resume upload failed.",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ResumeListView(APIView):
    """
    List all resumes uploaded by the logged-in user
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

        resumes = Resume.objects.filter(
            user=request.user
        ).order_by("-uploaded_at")

        serializer = ResumeUploadSerializer(
            resumes,
            many=True,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )