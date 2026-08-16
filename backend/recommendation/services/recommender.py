"""
recommendation/services/recommender.py

Main AI Recommendation Engine.

Generates:
1. Career recommendations
2. Skill recommendations
3. Course recommendations
4. Project recommendations
5. Learning roadmap
6. Resume improvement tips
"""

from recommendation.models import Recommendation

from recommendation.services.career import recommend_careers
from recommendation.services.courses import recommend_courses
from recommendation.services.projects import recommend_projects
from recommendation.services.roadmap import generate_roadmap
from recommendation.services.resume_tips import generate_resume_tips


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def _normalize_skills(skills):
    """
    Convert resume skills into a clean list.
    """

    if not skills:
        return []

    # If skills are stored as a string
    if isinstance(skills, str):
        return [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]

    # If skills are stored as a list/tuple
    if isinstance(skills, (list, tuple)):
        return [
            str(skill).strip()
            for skill in skills
            if str(skill).strip()
        ]

    return []


def _safe_list(value):
    """
    Make sure a value is always returned as a list.
    """

    if value is None:
        return []

    if isinstance(value, list):
        return value

    if isinstance(value, tuple):
        return list(value)

    try:
        return list(value)
    except (TypeError, ValueError):
        return []


# ==========================================================
# MAIN RECOMMENDATION ENGINE
# ==========================================================

def generate_recommendations(
    resume,
    ats_analysis=None,
):
    """
    Generate and save complete recommendations
    for a resume.
    """

    # ======================================================
    # 1. RESUME SKILLS
    # ======================================================

    skills = _normalize_skills(
        resume.skills
    )

    print(
        "Resume skills:",
        skills
    )

    # ======================================================
    # 2. CAREER RECOMMENDATIONS
    # ======================================================

    try:

        careers = recommend_careers(
            skills
        )

    except Exception as error:

        print(
            "Career recommendation error:",
            error
        )

        careers = []

    careers = _safe_list(careers)

    print(
        "Recommended careers:",
        careers
    )

    # ======================================================
    # 3. COURSE RECOMMENDATIONS
    # ======================================================

    try:

        courses = recommend_courses(
            careers
        )

    except Exception as error:

        print(
            "Course recommendation error:",
            error
        )

        courses = []

    courses = _safe_list(courses)

    print(
        "Recommended courses:",
        courses
    )

    # ======================================================
    # 4. PROJECT RECOMMENDATIONS
    # ======================================================

    try:

        projects = recommend_projects(
            careers
        )

    except Exception as error:

        print(
            "Project recommendation error:",
            error
        )

        projects = []

    projects = _safe_list(projects)

    print(
        "Recommended projects:",
        projects
    )

    # ======================================================
    # 5. LEARNING ROADMAP
    # ======================================================

    roadmap = {}

    for career in careers:

        try:

            roadmap[str(career)] = (
                generate_roadmap(career)
            )

        except Exception as error:

            print(
                "Roadmap error:",
                career,
                error
            )

            roadmap[str(career)] = []

    # ======================================================
    # 6. RESUME IMPROVEMENT TIPS
    # ======================================================

    if ats_analysis:

        try:

            resume_tips = generate_resume_tips(
                ats_analysis
            )

        except Exception as error:

            print(
                "Resume tips error:",
                error
            )

            resume_tips = []

    else:

        resume_tips = []

    resume_tips = _safe_list(
        resume_tips
    )

    print(
        "Resume tips:",
        resume_tips
    )

    # ======================================================
    # 7. MISSING SKILLS
    # ======================================================

    missing_skills = []

    if ats_analysis:

        try:

            missing_skills = _normalize_skills(
                ats_analysis.missing_skills
            )

        except Exception as error:

            print(
                "Missing skills error:",
                error
            )

            missing_skills = []

    print(
        "Recommended skills:",
        missing_skills
    )

    # ======================================================
    # 8. BUILD DATABASE DATA
    # ======================================================

    recommendation_data = {

        "recommended_roles": careers,

        "recommended_skills": missing_skills,

        "recommended_courses": courses,

        "recommended_projects": projects,

        "learning_roadmap": roadmap,

        "resume_tips": resume_tips,
    }

    # ======================================================
    # 9. SAVE / UPDATE RECOMMENDATION
    # ======================================================

    try:

        recommendation, created = (
            Recommendation.objects.update_or_create(

                resume=resume,

                defaults=recommendation_data,
            )
        )

    except Exception as error:

        print(
            "Recommendation database error:",
            error
        )

        raise error

    # ======================================================
    # 10. RETURN COMPLETE API DATA
    # ======================================================

    return {

        "id": recommendation.id,

        "resume_id": resume.id,

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

        "created": created,
    }