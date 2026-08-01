"""
Main ATS Analysis Service
"""

from .scoring import calculate_ats_score
from .strengths import analyze_strengths
from .suggestions import generate_suggestions


def analyze_resume(resume):
    """
    Perform complete ATS analysis for a resume.

    Returns a dictionary compatible with the ATSAnalysis model.
    """

    # -----------------------------
    # Calculate Scores
    # -----------------------------
    score_data = calculate_ats_score(resume)

    # -----------------------------
    # Analyze Resume
    # -----------------------------
    analysis = analyze_strengths(resume)

    # -----------------------------
    # Generate Suggestions
    # -----------------------------
    recommendations = generate_suggestions(
        resume,
        analysis,
    )

    # -----------------------------
    # Merge Everything
    # -----------------------------
    result = {
        # Overall Score
        "ats_score": score_data["ats_score"],

        # Individual Scores
        "keyword_score": score_data["keyword_score"],
        "skill_score": score_data["skill_score"],
        "education_score": score_data["education_score"],
        "experience_score": score_data["experience_score"],
        "project_score": score_data["project_score"],
        "certification_score": score_data["certification_score"],
        "format_score": score_data["format_score"],

        # Analysis
        "strengths": analysis["strengths"],
        "weaknesses": analysis["weaknesses"],
        "missing_skills": analysis["missing_skills"],

        # Recommendations
        "recommendations": recommendations,
    }

    return result