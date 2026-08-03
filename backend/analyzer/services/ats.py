"""
Main ATS Analysis Service
"""

from .scoring import calculate_ats_score
from .strengths import analyze_strengths
from .suggestions import generate_suggestions


def analyze_resume(resume):
    """
    Analyze a resume and return data compatible
    with the ATSAnalysis model.
    """

    # ----------------------------------------
    # Score Calculation
    # ----------------------------------------
    score_data = calculate_ats_score(resume)

    # ----------------------------------------
    # Strength / Weakness Analysis
    # ----------------------------------------
    analysis = analyze_strengths(resume)

    # ----------------------------------------
    # AI Recommendations
    # ----------------------------------------
    recommendations = generate_suggestions(
        resume,
        analysis,
    )

    return {

        # Overall ATS Score
        "ats_score": score_data.get(
            "ats_score",
            0,
        ),

        # Individual Scores
        "keyword_score": score_data.get(
            "keyword_score",
            0,
        ),

        "skill_score": score_data.get(
            "skill_score",
            0,
        ),

        "education_score": score_data.get(
            "education_score",
            0,
        ),

        "experience_score": score_data.get(
            "experience_score",
            0,
        ),

        "project_score": score_data.get(
            "project_score",
            0,
        ),

        "certification_score": score_data.get(
            "certification_score",
            0,
        ),

        "format_score": score_data.get(
            "format_score",
            0,
        ),

        # Analysis
        "strengths": analysis.get(
            "strengths",
            [],
        ),

        "weaknesses": analysis.get(
            "weaknesses",
            [],
        ),

        "missing_skills": analysis.get(
            "missing_skills",
            [],
        ),

        # Recommendations
        "recommendations": recommendations
        if recommendations
        else [],
    }