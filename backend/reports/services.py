from .models import Report


def build_report(resume, match_score=0):
    """
    Generate and store a resume analysis report.
    """

    report = Report.objects.create(
        user=resume.user,
        resume=resume,
        ats_score=resume.ats_score,
        match_score=match_score,
        parsed_data={
            "full_name": resume.full_name,
            "email": resume.email,
            "phone": resume.phone,
            "location": resume.location,
            "linkedin": resume.linkedin,
            "github": resume.github,
            "portfolio": resume.portfolio,
            "skills": resume.skills,
            "education": resume.education,
            "experience": resume.experience,
            "projects": resume.projects,
            "certifications": resume.certifications,
            "languages": resume.languages,
            "missing_skills": resume.missing_skills,
        },
        recommendations=resume.ai_recommendations,
    )

    return report