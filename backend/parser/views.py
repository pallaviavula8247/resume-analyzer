from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Resume
from .serializers import (
    ResumeUploadSerializer,
    ResumeSerializer,
)
from .utils import extract_text
from .services import parse_resume


# ==========================================
# Upload Resume
# ==========================================
class ResumeUploadView(APIView):
    """
    Upload Resume, Extract Text and Parse Resume
    """

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        serializer = ResumeUploadSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            # ==========================================
            # 1. SAVE UPLOADED RESUME
            # ==========================================

            resume = serializer.save(
                user=request.user
            )

            print("\n==========================================")
            print("NEW RESUME UPLOADED")
            print("Resume ID:", resume.id)
            print("File:", resume.resume_file.name)
            print("User:", request.user.username)
            print("==========================================")

            # ==========================================
            # 2. EXTRACT TEXT FROM THIS PDF
            # ==========================================

            extracted_text = extract_text(
                resume.resume_file.path
            )

            # ==========================================
            # DEBUG - SHOW EXTRACTED TEXT
            # ==========================================

            print("\n========== EXTRACTED RESUME TEXT ==========")
            print(extracted_text)
            print("========== END EXTRACTED TEXT ==========\n")

            # ==========================================
            # 3. CHECK EXTRACTION
            # ==========================================

            if not extracted_text or not extracted_text.strip():

                return Response(
                    {
                        "success": False,
                        "message": (
                            "Unable to extract text from "
                            "the uploaded resume."
                        ),
                        "resume_id": resume.id,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # ==========================================
            # 4. PARSE THIS RESUME TEXT
            # ==========================================

            parsed_data = parse_resume(
                extracted_text
            )

            # ==========================================
            # DEBUG - SHOW PARSED DATA
            # ==========================================

            print("\n========== PARSED RESUME DATA ==========")
            print("Resume ID:", resume.id)
            print("Full Name:", parsed_data.get("full_name"))
            print("Email:", parsed_data.get("email"))
            print("Phone:", parsed_data.get("phone"))
            print("Skills:", parsed_data.get("skills"))
            print("Education:", parsed_data.get("education"))
            print("Experience:", parsed_data.get("experience"))
            print("Projects:", parsed_data.get("projects"))
            print("Certifications:", parsed_data.get("certifications"))
            print("Languages:", parsed_data.get("languages"))
            print("========================================\n")

            # ==========================================
            # 5. SAVE EXTRACTED TEXT
            # ==========================================

            resume.extracted_text = extracted_text

            # ==========================================
            # 6. SAVE PERSONAL INFORMATION
            # ==========================================

            resume.full_name = parsed_data.get(
                "full_name",
                "",
            )

            resume.email = parsed_data.get(
                "email",
                "",
            )

            resume.phone = parsed_data.get(
                "phone",
                "",
            )

            resume.location = parsed_data.get(
                "location",
                "",
            )

            resume.linkedin = parsed_data.get(
                "linkedin",
                "",
            )

            resume.github = parsed_data.get(
                "github",
                "",
            )

            resume.portfolio = parsed_data.get(
                "portfolio",
                "",
            )

            # ==========================================
            # 7. SAVE RESUME SECTIONS
            # ==========================================

            resume.skills = parsed_data.get(
                "skills",
                [],
            )

            resume.education = parsed_data.get(
                "education",
                [],
            )

            resume.experience = parsed_data.get(
                "experience",
                [],
            )

            resume.projects = parsed_data.get(
                "projects",
                [],
            )

            resume.certifications = parsed_data.get(
                "certifications",
                [],
            )

            resume.languages = parsed_data.get(
                "languages",
                [],
            )

            # ==========================================
            # 8. SAVE ANALYSIS DATA
            # ==========================================

            resume.ats_score = parsed_data.get(
                "ats_score",
                0,
            )

            resume.missing_skills = parsed_data.get(
                "missing_skills",
                [],
            )

            resume.ai_recommendations = parsed_data.get(
                "recommendations",
                [],
            )

            # ==========================================
            # 9. SAVE EVERYTHING
            # ==========================================

            resume.save()

            print("\n==========================================")
            print("RESUME SAVED SUCCESSFULLY")
            print("Resume ID:", resume.id)
            print("Name:", resume.full_name)
            print("Skills:", resume.skills)
            print("Experience:", resume.experience)
            print("==========================================\n")

            # ==========================================
            # 10. RETURN RESPONSE
            # ==========================================

            return Response(
                {
                    "success": True,
                    "message": (
                        "Resume uploaded successfully."
                    ),
                    "data": {
                        "resume_id": resume.id,
                        "parsed_data": parsed_data,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:

            print("\n==========================================")
            print("RESUME UPLOAD ERROR")
            print(str(e))
            print("==========================================\n")

            return Response(
                {
                    "success": False,
                    "message": "Resume upload failed.",
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# ==========================================
# Resume List
# ==========================================
class ResumeListView(APIView):
    """
    List all resumes uploaded by the logged-in user.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):

        resumes = Resume.objects.filter(
            user=request.user
        ).order_by(
            "-uploaded_at"
        )

        serializer = ResumeSerializer(
            resumes,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": resumes.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )