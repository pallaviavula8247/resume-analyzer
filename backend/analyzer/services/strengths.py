"""
Resume Strengths & Weaknesses Analyzer
"""


def analyze_strengths(resume):
    """
    Analyze resume strengths, weaknesses, and missing skills.
    """

    strengths = []
    weaknesses = []
    missing_skills = []

    # -----------------------------
    # Personal Information
    # -----------------------------
    if resume.linkedin:
        strengths.append("LinkedIn profile added")
    else:
        weaknesses.append("LinkedIn profile is missing")

    if resume.github:
        strengths.append("GitHub profile added")
    else:
        weaknesses.append("GitHub profile is missing")

    if resume.portfolio:
        strengths.append("Portfolio website available")
    else:
        weaknesses.append("Portfolio website is missing")

    # -----------------------------
    # Skills
    # -----------------------------
    skill_count = len(resume.skills)

    if skill_count >= 8:
        strengths.append("Strong technical skill set")
    elif skill_count >= 5:
        strengths.append("Good technical skills")
    else:
        weaknesses.append("Add more technical skills")

    # -----------------------------
    # Education
    # -----------------------------
    if resume.education:
        strengths.append("Education details included")
    else:
        weaknesses.append("Education section missing")

    # -----------------------------
    # Experience
    # -----------------------------
    if resume.experience:
        strengths.append("Work experience included")
    else:
        weaknesses.append("Work experience not provided")

    # -----------------------------
    # Projects
    # -----------------------------
    if resume.projects:
        strengths.append("Projects showcase practical experience")
    else:
        weaknesses.append("Projects section missing")

    # -----------------------------
    # Certifications
    # -----------------------------
    if resume.certifications:
        strengths.append("Certifications included")
    else:
        weaknesses.append("No certifications found")

    # -----------------------------
    # Common ATS Skills
    # -----------------------------
    required_skills = [
        "Python",
        "SQL",
        "Git",
        "Docker",
        "REST API",
    ]

    resume_skills = {
        skill.lower()
        for skill in resume.skills
    }

    for skill in required_skills:

        if skill.lower() not in resume_skills:
            missing_skills.append(skill)

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "missing_skills": missing_skills,
    }