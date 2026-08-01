"""
detail.py

Resume detail service.
"""

from parser.models import Resume
from analyzer.models import ATSAnalysis, JobMatch
from recommendation.models import Recommendation


def get_resume_detail(user, resume_id):
    """
    Return complete details of a resume.
    """

    try:
        resume = Resume.objects.get(
            id=resume_id,
            user=user,
        )

    except Resume.DoesNotExist:
        return None

    ats = (
        ATSAnalysis.objects
        .filter(resume=resume)
        .first()
    )

    job_match = (
        JobMatch.objects
        .filter(resume=resume)
        .order_by("-created_at")
        .first()
    )

    recommendation = (
        Recommendation.objects
        .filter(resume=resume)
        .first()
    )

    return {

        "resume": {
            "id": resume.id,
            "full_name": resume.full_name,
            "email": resume.email,
            "phone": resume.phone,
            "location": resume.location,
            "skills": resume.skills,
            "education": resume.education,
            "experience": resume.experience,
            "projects": resume.projects,
            "certifications": resume.certifications,
            "uploaded_at": resume.uploaded_at,
        },

        "ats_analysis": ats,

        "job_match": job_match,

        "recommendation": recommendation,
    }