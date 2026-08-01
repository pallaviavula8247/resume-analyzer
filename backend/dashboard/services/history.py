"""
history.py

Resume history service.
"""

from parser.models import Resume
from analyzer.models import ATSAnalysis


def get_resume_history(user):
    """
    Return all resumes uploaded by the user.
    """

    resumes = (
        Resume.objects
        .filter(user=user)
        .order_by("-uploaded_at")
    )

    history = []

    for resume in resumes:

        analysis = (
            ATSAnalysis.objects
            .filter(resume=resume)
            .first()
        )

        history.append({
            "id": resume.id,
            "full_name": resume.full_name,
            "email": resume.email,
            "uploaded_at": resume.uploaded_at,
            "ats_score": analysis.ats_score if analysis else 0,
        })

    return history