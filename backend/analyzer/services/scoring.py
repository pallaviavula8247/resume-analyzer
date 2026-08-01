"""
ATS Resume Scoring Service
"""

MAX_SCORE = 100


def calculate_ats_score(resume):
    """
    Calculate ATS score using weighted sections.
    """

    score = 0

    # -------------------------
    # Personal Information (20)
    # -------------------------
    personal_score = 0

    if resume.full_name:
        personal_score += 3

    if resume.email:
        personal_score += 3

    if resume.phone:
        personal_score += 3

    if resume.location:
        personal_score += 2

    if resume.linkedin:
        personal_score += 3

    if resume.github:
        personal_score += 3

    if resume.portfolio:
        personal_score += 3

    # -------------------------
    # Skills (25)
    # -------------------------
    skills_count = len(resume.skills)

    if skills_count >= 10:
        skill_score = 25
    elif skills_count >= 8:
        skill_score = 20
    elif skills_count >= 6:
        skill_score = 15
    elif skills_count >= 4:
        skill_score = 10
    elif skills_count >= 2:
        skill_score = 5
    else:
        skill_score = 0

    # -------------------------
    # Education (15)
    # -------------------------
    education_score = 15 if resume.education else 0

    # -------------------------
    # Experience (15)
    # -------------------------
    experience_score = 15 if resume.experience else 0

    # -------------------------
    # Projects (10)
    # -------------------------
    project_score = 10 if resume.projects else 0

    # -------------------------
    # Certifications (5)
    # -------------------------
    certification_score = 5 if resume.certifications else 0

    # -------------------------
    # Resume Format (10)
    # -------------------------
    format_score = 0

    if resume.extracted_text:

        words = len(resume.extracted_text.split())

        if words >= 300:
            format_score = 10
        elif words >= 200:
            format_score = 8
        elif words >= 100:
            format_score = 6
        else:
            format_score = 4

    # -------------------------
    # Final Score
    # -------------------------
    score = (
        personal_score
        + skill_score
        + education_score
        + experience_score
        + project_score
        + certification_score
        + format_score
    )

    score = min(score, MAX_SCORE)

    return {
        "ats_score": score,
        "keyword_score": 0,
        "skill_score": skill_score,
        "education_score": education_score,
        "experience_score": experience_score,
        "project_score": project_score,
        "certification_score": certification_score,
        "format_score": format_score,
    }