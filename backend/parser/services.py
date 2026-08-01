"""
Resume Parsing Service

Combines all parser modules and returns
structured resume information.
"""

from parser.parsers.personal import extract_personal_info
from parser.parsers.skills import extract_skills
from parser.parsers.education import extract_education
from parser.parsers.experience import extract_experience
from parser.parsers.projects import extract_projects
from parser.parsers.certifications import extract_certifications
from parser.parsers.languages import extract_languages


def calculate_ats_score(
    skills,
    education,
    experience,
    projects,
    certifications,
):
    """
    Calculate a basic ATS score.
    """

    score = 0

    # Skills (40 Marks)

    score += min(len(skills) * 4, 40)

    # Education (20 Marks)

    if education:
        score += 20

    # Experience (15 Marks)

    if experience:
        score += 15

    # Projects (15 Marks)

    if projects:
        score += 15

    # Certifications (10 Marks)

    if certifications:
        score += 10

    return min(score, 100)


def get_missing_skills(skills):
    """
    Placeholder for future Job Matching.
    """

    REQUIRED_SKILLS = [
        "Python",
        "SQL",
        "Git",
        "REST API",
        "Docker",
    ]

    missing = []

    for skill in REQUIRED_SKILLS:

        if skill not in skills:
            missing.append(skill)

    return missing


def generate_recommendations(
    ats_score,
    missing_skills,
    projects,
    certifications,
):
    """
    Generate resume recommendations.
    """

    recommendations = []

    if ats_score < 60:

        recommendations.append(
            "Improve your resume by adding more technical skills."
        )

    if missing_skills:

        recommendations.append(
            "Learn these important skills: "
            + ", ".join(missing_skills)
        )

    if not projects:

        recommendations.append(
            "Include academic or personal projects."
        )

    if not certifications:

        recommendations.append(
            "Add professional certifications."
        )

    if ats_score >= 80:

        recommendations.append(
            "Excellent resume. Keep it updated."
        )

    return recommendations


def parse_resume(text):
    """
    Parse complete resume.
    """

    # -----------------------------
    # Personal Information
    # -----------------------------

    personal = extract_personal_info(text)

    # -----------------------------
    # Skills
    # -----------------------------

    skills = extract_skills(text)

    # -----------------------------
    # Education
    # -----------------------------

    education = extract_education(text)

    # -----------------------------
    # Experience
    # -----------------------------

    experience = extract_experience(text)

    # -----------------------------
    # Projects
    # -----------------------------

    projects = extract_projects(text)

    # -----------------------------
    # Certifications
    # -----------------------------

    certifications = extract_certifications(text)

    # -----------------------------
    # Languages
    # -----------------------------

    languages = extract_languages(text)

    # -----------------------------
    # ATS Score
    # -----------------------------

    ats_score = calculate_ats_score(
        skills,
        education,
        experience,
        projects,
        certifications,
    )

    # -----------------------------
    # Missing Skills
    # -----------------------------

    missing_skills = get_missing_skills(
        skills
    )

    # -----------------------------
    # AI Recommendations
    # -----------------------------

    recommendations = generate_recommendations(
        ats_score,
        missing_skills,
        projects,
        certifications,
    )

    # -----------------------------
    # Final JSON
    # -----------------------------

    return {

        # Personal Information
        "full_name": personal.get(
            "full_name",
            "",
        ),

        "email": personal.get(
            "email",
            "",
        ),

        "phone": personal.get(
            "phone",
            "",
        ),

        "location": personal.get(
            "location",
            "",
        ),

        "linkedin": personal.get(
            "linkedin",
            "",
        ),

        "github": personal.get(
            "github",
            "",
        ),

        "portfolio": personal.get(
            "portfolio",
            "",
        ),

        # Resume Sections
        "skills": skills,

        "education": education,

        "experience": experience,

        "projects": projects,

        "certifications": certifications,

        "languages": languages,

        # Analysis
        "ats_score": ats_score,

        "missing_skills": missing_skills,

        "recommendations": recommendations,
    }