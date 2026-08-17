"""
Resume Parsing Service

Responsible ONLY for extracting structured information
from the text of the uploaded resume.

This module must NOT:
- calculate ATS scores
- generate job matches
- generate recommendations
- invent missing skills
- insert default resume data

The uploaded resume is the single source of truth.
"""

from parser.parsers.personal import extract_personal_info
from parser.parsers.skills import extract_skills
from parser.parsers.education import extract_education
from parser.parsers.experience import extract_experience
from parser.parsers.projects import extract_projects
from parser.parsers.certifications import extract_certifications
from parser.parsers.languages import extract_languages


def parse_resume(text):
    """
    Parse the actual extracted resume text.

    This function ONLY extracts information that exists
    in the uploaded resume.

    Args:
        text (str):
            Text extracted from the uploaded PDF.

    Returns:
        dict:
            Structured resume information.
    """

    # =========================================================
    # EMPTY RESUME CHECK
    # =========================================================

    if not text or not text.strip():

        return {
            "full_name": "",
            "email": "",
            "phone": "",
            "location": "",
            "linkedin": "",
            "github": "",
            "portfolio": "",
            "skills": [],
            "education": [],
            "experience": [],
            "projects": [],
            "certifications": [],
            "languages": [],
        }

    # =========================================================
    # PERSONAL INFORMATION
    # =========================================================

    personal = extract_personal_info(text)

    # =========================================================
    # SKILLS
    # =========================================================

    skills = extract_skills(text)

    # =========================================================
    # EDUCATION
    # =========================================================

    education = extract_education(text)

    # =========================================================
    # EXPERIENCE
    # =========================================================

    experience = extract_experience(text)

    # =========================================================
    # PROJECTS
    # =========================================================

    projects = extract_projects(text)

    # =========================================================
    # CERTIFICATIONS
    # =========================================================

    certifications = extract_certifications(text)

    # =========================================================
    # LANGUAGES
    # =========================================================

    languages = extract_languages(text)

    # =========================================================
    # RETURN ONLY EXTRACTED DATA
    # =========================================================

    return {

        # Personal information
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

        # Resume sections
        "skills": skills,

        "education": education,

        "experience": experience,

        "projects": projects,

        "certifications": certifications,

        "languages": languages,
    }