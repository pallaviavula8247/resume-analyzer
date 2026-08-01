"""
charts.py

Generate dashboard chart data.
"""

from parser.models import Resume
from analyzer.models import ATSAnalysis, JobMatch


def get_dashboard_charts(user):
    """
    Generate dashboard chart data.
    """

    # ==================================================
    # ATS Score Chart
    # ==================================================

    ats_chart = {
        "labels": [],
        "scores": [],
    }

    analyses = (
        ATSAnalysis.objects
        .filter(resume__user=user)
        .order_by("resume__id")
    )

    for analysis in analyses:
        ats_chart["labels"].append(
            f"Resume {analysis.resume.id}"
        )
        ats_chart["scores"].append(
            analysis.ats_score
        )

    # ==================================================
    # Job Match Chart
    # ==================================================

    job_match_chart = {
        "labels": [],
        "scores": [],
    }

    matches = (
        JobMatch.objects
        .filter(resume__user=user)
        .order_by("created_at")
    )

    for match in matches:
        job_match_chart["labels"].append(
            match.job_title or f"Job {match.id}"
        )

        job_match_chart["scores"].append(
            match.match_score
        )

    # ==================================================
    # Skills Distribution (Latest Resume Only)
    # ==================================================

    skills_chart = {
        "labels": [],
        "counts": [],
    }

    latest_resume = (
        Resume.objects
        .filter(user=user)
        .order_by("-uploaded_at")
        .first()
    )

    if latest_resume:

        skills = latest_resume.skills or []

        # If stored as text
        if isinstance(skills, str):

            skills = [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ]

        # If stored as JSON list
        elif not isinstance(skills, list):

            skills = []

        skills_chart["labels"] = skills
        skills_chart["counts"] = [1] * len(skills)

    # ==================================================
    # Resume Upload Timeline
    # ==================================================

    timeline_chart = {
        "labels": [],
        "uploads": [],
    }

    resumes = (
        Resume.objects
        .filter(user=user)
        .order_by("uploaded_at")
    )

    for resume in resumes:

        timeline_chart["labels"].append(
            resume.uploaded_at.strftime("%d-%b")
        )

        timeline_chart["uploads"].append(1)

    # ==================================================
    # Final Response
    # ==================================================

    return {
        "ats_chart": ats_chart,
        "job_match_chart": job_match_chart,
        "skills_chart": skills_chart,
        "timeline_chart": timeline_chart,
    }