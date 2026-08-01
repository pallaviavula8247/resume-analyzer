"""
recommender.py

Main AI Recommendation Engine

This module combines:
1. Career Recommendations
2. Course Recommendations
3. Project Recommendations
4. Learning Roadmap
5. Resume Improvement Tips
"""

from recommendation.services.career import recommend_careers
from recommendation.services.courses import recommend_courses
from recommendation.services.projects import recommend_projects
from recommendation.services.roadmap import generate_roadmap
from recommendation.services.resume_tips import generate_resume_tips


def generate_recommendations(resume, ats_analysis):
    """
    Generate complete recommendations for a resume.

    Parameters
    ----------
    resume : Resume object
    ats_analysis : ATSAnalysis object

    Returns
    -------
    dict
    """

    # ---------------------------------------
    # Extract Resume Skills
    # ---------------------------------------

    skills = resume.skills or []

    if isinstance(skills, str):
        skills = [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]

    # ---------------------------------------
    # Career Recommendations
    # ---------------------------------------

    careers = recommend_careers(skills)

    # ---------------------------------------
    # Course Recommendations
    # ---------------------------------------

    courses = recommend_courses(careers)

    # ---------------------------------------
    # Project Recommendations
    # ---------------------------------------

    projects = recommend_projects(careers)

    # ---------------------------------------
    # Learning Roadmap
    # ---------------------------------------

    roadmap = {}

    for career in careers:
        roadmap[career] = generate_roadmap(career)

    # ---------------------------------------
    # Resume Tips
    # ---------------------------------------

    resume_tips = generate_resume_tips(
        ats_analysis
    )

    # ---------------------------------------
    # Final Response
    # ---------------------------------------

    return {
        "recommended_careers": careers,
        "recommended_courses": courses,
        "recommended_projects": projects,
        "learning_roadmap": roadmap,
        "resume_tips": resume_tips,
    }