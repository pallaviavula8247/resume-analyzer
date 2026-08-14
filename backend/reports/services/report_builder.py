"""
reports/services/report_builder.py

Build complete report data for PDF generation.
"""

from datetime import datetime

from parser.models import Resume
from analyzer.models import ATSAnalysis, JobMatch
from recommendation.models import Recommendation


def get_ats_category(score):
    """
    Convert ATS score into a readable category.
    """

    if score is None:
        return "Not Analyzed"

    score = float(score)

    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Very Good"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Needs Improvement"
    else:
        return "Poor"


def build_report(resume_id):
    """
    Build complete report data for a resume.

    Parameters
    ----------
    resume_id : int
        Resume primary key.

    Returns
    -------
    dict or None
    """

    # ==================================================
    # Get Resume
    # ==================================================

    try:
        resume = Resume.objects.get(id=resume_id)
    except Resume.DoesNotExist:
        return None

    # ==================================================
    # Get ATS Analysis
    # ==================================================

    ats = (
        ATSAnalysis.objects
        .filter(resume=resume)
        .order_by("-id")
        .first()
    )

    # ==================================================
    # Get Job Matches
    # ==================================================

    job_matches = (
        JobMatch.objects
        .filter(resume=resume)
        .order_by("-id")
    )

    # ==================================================
    # Get Phase 7 Recommendation
    # ==================================================

    recommendation = (
        Recommendation.objects
        .filter(resume=resume)
        .first()
    )

    # ==================================================
    # ATS Score
    # ==================================================

    ats_score = (
        ats.ats_score
        if ats and ats.ats_score is not None
        else 0
    )

    # ==================================================
    # Missing Skills
    # ==================================================

    missing_skills = []

    if ats:
        missing_skills = ats.missing_skills or []

    # ==================================================
    # Candidate Information
    # ==================================================

    candidate = {
        "resume_id": resume.id,
        "name": resume.full_name or "",
        "email": resume.email or "",
        "phone": resume.phone or "",
        "location": resume.location or "",
        "linkedin": resume.linkedin or "",
        "github": resume.github or "",
        "portfolio": resume.portfolio or "",
        "resume_file": (
            resume.resume_file.url
            if resume.resume_file
            else ""
        ),
    }

    # ==================================================
    # Resume Information
    # ==================================================

    resume_information = {
        "education": resume.education or [],
        "experience": resume.experience or [],
        "skills": resume.skills or [],
        "projects": resume.projects or [],
        "certifications": resume.certifications or [],
        "languages": resume.languages or [],
        "uploaded_at": (
            resume.uploaded_at.strftime("%d %B %Y, %I:%M %p")
            if resume.uploaded_at
            else ""
        ),
    }

    # ==================================================
    # ATS Analysis Section
    # ==================================================

    ats_analysis = None

    if ats:

        ats_analysis = {
            "ats_score": ats.ats_score or 0,

            "keyword_score": (
                ats.keyword_score or 0
            ),

            "skill_score": (
                ats.skill_score or 0
            ),

            "education_score": (
                ats.education_score or 0
            ),

            "experience_score": (
                ats.experience_score or 0
            ),

            "project_score": (
                ats.project_score or 0
            ),

            "certification_score": (
                ats.certification_score or 0
            ),

            "format_score": (
                ats.format_score or 0
            ),

            "strengths": (
                ats.strengths or []
            ),

            "weaknesses": (
                ats.weaknesses or []
            ),

            "missing_skills": (
                ats.missing_skills or []
            ),

            "recommendations": (
                ats.recommendations or []
            ),

            "analyzed_at": (
                ats.created_at.strftime(
                    "%d %B %Y, %I:%M %p"
                )
                if hasattr(ats, "created_at")
                and ats.created_at
                else ""
            ),
        }

    # ==================================================
    # Job Match Section
    # ==================================================

    job_match_data = []

    for match in job_matches:

        job_match_data.append(
            {
                "job_title": (
                    match.job_title or ""
                ),

                "description": (
                    match.description or ""
                    if hasattr(match, "description")
                    else ""
                ),

                "match_score": (
                    match.match_score or 0
                ),

                "match_level": (
                    match.match_level
                    or "Not Available"
                ),

                "matched_skills": (
                    match.matched_skills or []
                ),

                "missing_skills": (
                    match.missing_skills or []
                ),

                "extra_skills": (
                    match.extra_skills or []
                ),

                "recommendations": (
                    match.recommendations or []
                ),

                "created_at": (
                    match.created_at.strftime(
                        "%d %B %Y, %I:%M %p"
                    )
                    if hasattr(match, "created_at")
                    and match.created_at
                    else ""
                ),
            }
        )

    # ==================================================
    # Phase 7 AI Recommendations
    # ==================================================

    recommendations = {
        "recommended_roles": [],
        "recommended_skills": [],
        "recommended_courses": [],
        "recommended_projects": [],
        "learning_roadmap": {},
        "resume_tips": [],
    }

    if recommendation:

        recommendations = {
            "recommended_roles": (
                recommendation.recommended_roles
                or []
            ),

            "recommended_skills": (
                recommendation.recommended_skills
                or []
            ),

            "recommended_courses": (
                recommendation.recommended_courses
                or []
            ),

            "recommended_projects": (
                recommendation.recommended_projects
                or []
            ),

            "learning_roadmap": (
                recommendation.learning_roadmap
                or {}
            ),

            "resume_tips": (
                recommendation.resume_tips
                or []
            ),
        }

    # ==================================================
    # Summary
    # ==================================================

    summary = {
        "ats_score": ats_score,

        "ats_category": get_ats_category(
            ats_score
        )
        if ats
        else "Not Analyzed",

        "job_matches": job_matches.count(),

        "missing_skills": len(
            missing_skills
        ),
    }

    # ==================================================
    # Final Report
    # ==================================================

    report = {

        "report_info": {
            "title": "AI Resume Analyzer Report",

            "generated_at": datetime.now().strftime(
                "%d %B %Y, %I:%M %p"
            ),

            "version": "1.0",
        },

        "candidate": candidate,

        "resume_information": resume_information,

        "summary": summary,

        "ats_analysis": ats_analysis,

        "job_matches": job_match_data,

        "recommendations": recommendations,
    }

    return report