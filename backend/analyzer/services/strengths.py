"""
Resume Strength and Weakness Analysis
"""


def analyze_strengths(resume):

    strengths = []
    weaknesses = []
    missing_skills = []

    # ========================================================
    # SKILLS
    # ========================================================

    skills = getattr(
        resume,
        "skills",
        []
    )

    if isinstance(skills, dict):

        skills = list(
            skills.keys()
        )

    elif isinstance(skills, str):

        skills = [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]

    elif not isinstance(skills, list):

        skills = []


    skills = [
        str(skill).strip()
        for skill in skills
        if str(skill).strip()
    ]


    # ========================================================
    # STRENGTHS
    # ========================================================

    if skills:

        strengths.append(
            f"Resume contains {len(skills)} technical skills."
        )

        if any(
            skill.lower() == "python"
            for skill in skills
        ):

            strengths.append(
                "Python is included in the technical skill set."
            )

        if any(
            skill.lower() == "django"
            for skill in skills
        ):

            strengths.append(
                "Django experience supports backend development roles."
            )

        if any(
            skill.lower() == "react"
            for skill in skills
        ):

            strengths.append(
                "React experience supports frontend development roles."
            )

    else:

        weaknesses.append(
            "Technical skills could not be identified clearly."
        )


    # ========================================================
    # EDUCATION
    # ========================================================

    education = getattr(
        resume,
        "education",
        None
    )

    if education:

        strengths.append(
            "Education information is available in the resume."
        )

    else:

        weaknesses.append(
            "Education information should be clearly included."
        )


    # ========================================================
    # EXPERIENCE
    # ========================================================

    experience = getattr(
        resume,
        "experience",
        None
    )

    if experience:

        strengths.append(
            "Professional or practical experience is present."
        )

    else:

        weaknesses.append(
            "Add relevant internship, work, or practical experience."
        )


    # ========================================================
    # PROJECTS
    # ========================================================

    projects = getattr(
        resume,
        "projects",
        None
    )

    if projects:

        strengths.append(
            "Projects provide practical evidence of technical skills."
        )

    else:

        weaknesses.append(
            "Add relevant technical projects with measurable results."
        )


    # ========================================================
    # COMMON MISSING SKILLS
    # ========================================================

    skill_text = " ".join(
        skill.lower()
        for skill in skills
    )


    important_skills = [
        "python",
        "sql",
        "git",
        "rest api",
        "django",
        "react",
    ]


    for skill in important_skills:

        if skill not in skill_text:

            missing_skills.append(
                skill
            )


    # ========================================================
    # DEFAULT STRENGTH
    # ========================================================

    if not strengths:

        strengths.append(
            "Resume contains useful information for analysis."
        )


    # ========================================================
    # DEFAULT WEAKNESS
    # ========================================================

    if not weaknesses:

        weaknesses.append(
            "Continue improving measurable achievements and job-specific keywords."
        )


    return {

        "strengths": strengths,

        "weaknesses": weaknesses,

        "missing_skills": missing_skills,

    }

