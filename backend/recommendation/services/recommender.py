"""
recommendation/services/recommender.py

Main AI Recommendation Engine.

Combines:
1. Career Recommendations
2. Course Recommendations
3. Project Recommendations
4. Learning Roadmap
5. Resume Improvement Tips

This service generates recommendations and saves them
to the Recommendation model.
"""

from recommendation.models import Recommendation

from recommendation.services.career import recommend_careers
from recommendation.services.courses import recommend_courses
from recommendation.services.projects import recommend_projects
from recommendation.services.roadmap import generate_roadmap
from recommendation.services.resume_tips import generate_resume_tips


def _normalize_skills(skills):
    """
    Convert resume skills into a clean list.
    """

    if not skills:
        return []

    if isinstance(skills, str):
        return [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]

    if isinstance(skills, list):
        return [
            str(skill).strip()
            for skill in skills
            if str(skill).strip()
        ]

    return []


def generate_recommendations(resume, ats_analysis=None):
    """
    Generate complete AI recommendations for a resume.

    Parameters
    ----------
    resume : Resume
        Resume model instance.

    ats_analysis : ATSAnalysis, optional
        ATS analysis instance used to generate resume tips.

    Returns
    -------
    dict
        Complete recommendation data.
    """

    # ==================================================
    # 1. Extract Resume Skills
    # ==================================================

    skills = _normalize_skills(resume.skills)

    # ==================================================
    # 2. Career Recommendations
    # ==================================================

    careers = recommend_careers(skills)

    # Make sure careers is always a list
    if not isinstance(careers, list):
        careers = list(careers) if careers else []

    # ==================================================
    # 3. Course Recommendations
    # ==================================================

    courses = recommend_courses(careers)

    if not isinstance(courses, list):
        courses = list(courses) if courses else []

    # ==================================================
    # 4. Project Recommendations
    # ==================================================

    projects = recommend_projects(careers)

    if not isinstance(projects, list):
        projects = list(projects) if projects else []

    # ==================================================
    # 5. Learning Roadmap
    # ==================================================

    roadmap = {}

    for career in careers:

        try:
            roadmap[career] = generate_roadmap(career)
        except Exception:
            roadmap[career] = []

    # ==================================================
    # 6. Resume Improvement Tips
    # ==================================================

    if ats_analysis:
        try:
            resume_tips = generate_resume_tips(
                ats_analysis
            )
        except Exception:
            resume_tips = []
    else:
        resume_tips = []

    if not isinstance(resume_tips, list):
        resume_tips = list(resume_tips) if resume_tips else []

    # ==================================================
    # 7. Build Recommendation Data
    # ==================================================

    recommendation_data = {
        "recommended_roles": careers,
        "recommended_skills": (
            ats_analysis.missing_skills
            if ats_analysis and ats_analysis.missing_skills
            else []
        ),
        "recommended_courses": courses,
        "recommended_projects": projects,
        "learning_roadmap": roadmap,
        "resume_tips": resume_tips,
    }

    # ==================================================
    # 8. Save / Update Recommendation
    # ==================================================

    recommendation, created = (
        Recommendation.objects.update_or_create(
            resume=resume,
            defaults=recommendation_data,
        )
    )

    # ==================================================
    # 9. Return Complete Result
    # ==================================================

    return {
        "id": recommendation.id,
        "resume_id": resume.id,
        "recommended_roles": recommendation.recommended_roles,
        "recommended_skills": recommendation.recommended_skills,
        "recommended_courses": recommendation.recommended_courses,
        "recommended_projects": recommendation.recommended_projects,
        "learning_roadmap": recommendation.learning_roadmap,
        "resume_tips": recommendation.resume_tips,
        "created": created,
    }