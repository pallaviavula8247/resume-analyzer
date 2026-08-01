"""
ATS Recommendation Generator
"""


def generate_suggestions(resume, analysis):
    """
    Generate ATS improvement recommendations.

    Parameters
    ----------
    resume : Resume
        Parsed resume object.

    analysis : dict
        Output from analyze_strengths().
    """

    suggestions = []

    missing_skills = analysis.get("missing_skills", [])
    weaknesses = analysis.get("weaknesses", [])

    # ---------------------------------
    # Missing Skills
    # ---------------------------------
    if missing_skills:
        suggestions.append(
            "Add these important technical skills: "
            + ", ".join(missing_skills)
        )

    # ---------------------------------
    # Portfolio
    # ---------------------------------
    if not resume.portfolio:
        suggestions.append(
            "Create a portfolio website to showcase your projects."
        )

    # ---------------------------------
    # GitHub
    # ---------------------------------
    if not resume.github:
        suggestions.append(
            "Add your GitHub profile to demonstrate coding experience."
        )

    # ---------------------------------
    # LinkedIn
    # ---------------------------------
    if not resume.linkedin:
        suggestions.append(
            "Include your LinkedIn profile for professional visibility."
        )

    # ---------------------------------
    # Experience
    # ---------------------------------
    if not resume.experience:
        suggestions.append(
            "Include internships, freelance work, or project experience."
        )

    # ---------------------------------
    # Projects
    # ---------------------------------
    if not resume.projects:
        suggestions.append(
            "Add at least 2–3 technical projects with technologies used."
        )

    # ---------------------------------
    # Certifications
    # ---------------------------------
    if not resume.certifications:
        suggestions.append(
            "Earn certifications from Coursera, AWS, Google, or Microsoft."
        )

    # ---------------------------------
    # Skills
    # ---------------------------------
    if len(resume.skills) < 8:
        suggestions.append(
            "Increase your technical skills section with relevant tools and frameworks."
        )

    # ---------------------------------
    # Resume Length
    # ---------------------------------
    if resume.extracted_text:
        word_count = len(resume.extracted_text.split())

        if word_count < 250:
            suggestions.append(
                "Expand your resume with more achievements and project details."
            )

    # ---------------------------------
    # ATS Score Recommendation
    # ---------------------------------
    ats_score = getattr(resume, "ats_score", 0)

    if ats_score < 80:
        suggestions.append(
            "Improve ATS score by adding job-specific keywords from the job description."
        )

    # ---------------------------------
    # Remove duplicates
    # ---------------------------------
    suggestions = list(dict.fromkeys(suggestions))

    return suggestions