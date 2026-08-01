"""
AI Job Matching Engine
"""

from .extractor import extract_skills
from .similarity import compare_skills


def match_resume(resume_data, job_description):
    """
    Match a resume against a job description.

    Args:
        resume_data (dict):
            {
                "skills": [...]
            }

        job_description (str)

    Returns:
        dict
    """

    # -----------------------------
    # Resume Skills
    # -----------------------------
    resume_skills = resume_data.get(
        "skills",
        [],
    )

    # -----------------------------
    # Extract Job Skills
    # -----------------------------
    job_skills = extract_skills(
        job_description
    )

    # -----------------------------
    # Compare Skills
    # -----------------------------
    result = compare_skills(
        resume_skills,
        job_skills,
    )

    # -----------------------------
    # Recommendations
    # -----------------------------
    recommendations = []

    if result["missing_skills"]:
        recommendations.append(
            "Learn these missing skills: "
            + ", ".join(result["missing_skills"])
        )

    if result["match_score"] < 60:
        recommendations.append(
            "Improve your resume by adding projects using the missing technologies."
        )

    if result["match_score"] < 80:
        recommendations.append(
            "Customize your resume using keywords from the job description."
        )

    if result["match_score"] >= 80:
        recommendations.append(
            "Excellent match! Your resume closely matches the job requirements."
        )

    # -----------------------------
    # Final Response
    # -----------------------------
    result["recommendations"] = recommendations

    return result