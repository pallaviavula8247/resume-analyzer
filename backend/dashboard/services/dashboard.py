"""
dashboard/services/dashboard.py

Main Dashboard Service
Returns complete dashboard information for the logged-in user.
"""

from parser.models import Resume
from analyzer.models import ATSAnalysis, JobMatch
from recommendation.models import Recommendation

from .statistics import get_dashboard_statistics
from .charts import get_dashboard_charts


def get_dashboard_data(user):
    """
    Build complete dashboard data.
    """

    # ==========================================
    # User Profile
    # ==========================================

    user_data = {
        "id": user.id,
        "full_name": getattr(user, "full_name", ""),
        "email": getattr(user, "email", ""),
    }

    # ==========================================
    # Dashboard Statistics
    # ==========================================

    statistics = get_dashboard_statistics(user)

    # ==========================================
    # Dashboard Charts
    # ==========================================

    charts = get_dashboard_charts(user)

    # ==========================================
    # Latest Resume
    # ==========================================

    latest_resume = (
        Resume.objects
        .filter(user=user)
        .order_by("-uploaded_at")
        .first()
    )

    latest_resume_data = None
    latest_resume_id = None
    ats_data = None
    job_matches = []
    recommendations = []

    if latest_resume:

        latest_resume_id = latest_resume.id

        ats = (
            ATSAnalysis.objects
            .filter(resume=latest_resume)
            .first()
        )

        latest_resume_data = {
            "id": latest_resume.id,
            "full_name": latest_resume.full_name,
            "email": latest_resume.email,
            "phone": latest_resume.phone,
            "uploaded_at": latest_resume.uploaded_at,
        }

        if ats:

            ats_data = {
                "ats_score": ats.ats_score,
                "keyword_score": ats.keyword_score,
                "skill_score": ats.skill_score,
                "education_score": ats.education_score,
                "experience_score": ats.experience_score,
                "project_score": ats.project_score,
                "certification_score": ats.certification_score,
                "format_score": ats.format_score,
                "strengths": ats.strengths,
                "weaknesses": ats.weaknesses,
                "missing_skills": ats.missing_skills,
            }

        matches = (
            JobMatch.objects
            .filter(resume=latest_resume)
            .order_by("-created_at")[:5]
        )

        for match in matches:

            job_matches.append({
                "job_title": match.job_title,
                "match_score": match.match_score,
                "match_level": match.match_level,
            })

        recs = (
            Recommendation.objects
            .filter(resume=latest_resume)
            .order_by("-created_at")[:5]
        )

        for rec in recs:

            recommendations.append({
                "title": getattr(rec, "title", ""),
                "description": getattr(rec, "description", ""),
            })

    # ==========================================
    # Recent Activity
    # ==========================================

    recent_activity = []

    if latest_resume:
        recent_activity.append("Resume uploaded")

    if ats_data:
        recent_activity.append("ATS analysis completed")

    if job_matches:
        recent_activity.append("Job matching completed")

    if recommendations:
        recent_activity.append("AI recommendations generated")

    # ==========================================
    # Final Dashboard Response
    # ==========================================

    return {

        "user": user_data,

        "statistics": statistics,

        "charts": charts,

        "latest_resume_id": latest_resume_id,

        "latest_resume": latest_resume_data,

        "ats": ats_data,

        "job_matches": job_matches,

        "recommendations": recommendations,

        "recent_activity": recent_activity,

    }