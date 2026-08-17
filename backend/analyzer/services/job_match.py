"""
============================================================
RESUME AI - JOB MATCHING SERVICE
============================================================

Generates suitable job roles based on resume skills.
"""


def normalize_skills(resume):
    """
    Safely extract skills from Resume.skills.
    """

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

    return [
        str(skill).strip().lower()
        for skill in skills
        if str(skill).strip()
    ]


def has_skill(skills, *names):
    """
    Check whether any skill exists.
    """

    skill_text = " ".join(skills)

    for name in names:

        if name.lower() in skill_text:
            return True

    return False


def calculate_match_score(
    skills,
    required_skills
):
    """
    Calculate percentage match.
    """

    if not required_skills:

        return 0

    matched = 0

    for skill in required_skills:

        if has_skill(
            skills,
            skill
        ):

            matched += 1

    score = (
        matched /
        len(required_skills)
    ) * 100

    return round(score)


def create_job(
    title,
    required_skills,
    skills,
    company="Recommended Role",
    location="India",
    job_type="Full Time"
):
    """
    Create one job-match object.
    """

    score = calculate_match_score(
        skills,
        required_skills
    )

    matched_skills = [
        skill
        for skill in required_skills
        if has_skill(
            skills,
            skill
        )
    ]

    missing_skills = [
        skill
        for skill in required_skills
        if not has_skill(
            skills,
            skill
        )
    ]

    return {

        "title": title,

        "job_title": title,

        "role": title,

        "company": company,

        "company_name": company,

        "location": location,

        "job_type": job_type,

        "match_score": score,

        "match_percentage": score,

        "score": score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "required_skills": required_skills,

    }


def generate_job_matches(resume):
    """
    Generate suitable roles from resume skills.
    """

    skills = normalize_skills(
        resume
    )


    jobs = []


    # ========================================================
    # PYTHON DEVELOPER
    # ========================================================

    if has_skill(
        skills,
        "python"
    ):

        jobs.append(
            create_job(

                "Python Developer",

                [
                    "python",
                    "git",
                    "sql",
                ],

                skills,

                "Software Development",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # DJANGO DEVELOPER
    # ========================================================

    if has_skill(
        skills,
        "python"
    ) and has_skill(
        skills,
        "django"
    ):

        jobs.append(
            create_job(

                "Django Developer",

                [
                    "python",
                    "django",
                    "sql",
                    "rest api",
                ],

                skills,

                "Backend Development",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # PYTHON FULL STACK
    # ========================================================

    if (
        has_skill(
            skills,
            "python"
        )
        and
        has_skill(
            skills,
            "react",
            "react.js"
        )
    ):

        jobs.append(
            create_job(

                "Python Full Stack Developer",

                [
                    "python",
                    "django",
                    "react",
                    "javascript",
                    "sql",
                ],

                skills,

                "Full Stack Development",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # FRONTEND DEVELOPER
    # ========================================================

    if has_skill(
        skills,
        "html"
    ) and (
        has_skill(
            skills,
            "css"
        )
        or
        has_skill(
            skills,
            "javascript"
        )
        or
        has_skill(
            skills,
            "react",
            "react.js"
        )
    ):

        jobs.append(
            create_job(

                "Frontend Developer",

                [
                    "html",
                    "css",
                    "javascript",
                    "react",
                ],

                skills,

                "Frontend Development",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # BACKEND DEVELOPER
    # ========================================================

    if (
        has_skill(
            skills,
            "python",
            "django",
            "flask",
            "node",
            "node.js"
        )
    ):

        jobs.append(
            create_job(

                "Backend Developer",

                [
                    "python",
                    "django",
                    "sql",
                    "rest api",
                ],

                skills,

                "Backend Engineering",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # MACHINE LEARNING ENGINEER
    # ========================================================

    if has_skill(
        skills,
        "machine learning",
        "machinelearning",
        "ml",
        "scikit-learn",
        "sklearn"
    ):

        jobs.append(
            create_job(

                "Machine Learning Engineer",

                [
                    "python",
                    "machine learning",
                    "numpy",
                    "pandas",
                    "scikit-learn",
                ],

                skills,

                "AI / Machine Learning",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # DATA ANALYST
    # ========================================================

    if (
        has_skill(
            skills,
            "python"
        )
        and
        has_skill(
            skills,
            "sql"
        )
    ):

        jobs.append(
            create_job(

                "Data Analyst",

                [
                    "python",
                    "sql",
                    "pandas",
                    "excel",
                    "data analysis",
                ],

                skills,

                "Data Analytics",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # SOFTWARE ENGINEER
    # ========================================================

    if (
        has_skill(
            skills,
            "python",
            "java",
            "c",
            "javascript"
        )
    ):

        jobs.append(
            create_job(

                "Software Engineer",

                [
                    "programming",
                    "sql",
                    "git",
                    "data structures",
                ],

                skills,

                "Software Engineering",

                "India",

                "Full Time",
            )
        )


    # ========================================================
    # DEFAULT JOBS
    # ========================================================

    if not jobs:

        jobs = [

            create_job(

                "Junior Software Developer",

                [
                    "programming",
                    "sql",
                    "git",
                ],

                skills,

                "Software Development",

                "India",

                "Full Time",
            ),

            create_job(

                "Junior Python Developer",

                [
                    "python",
                    "sql",
                ],

                skills,

                "Python Development",

                "India",

                "Full Time",
            ),

            create_job(

                "Software Engineer",

                [
                    "programming",
                    "sql",
                ],

                skills,

                "Software Engineering",

                "India",

                "Full Time",
            ),

        ]


    # ========================================================
    # SORT BY MATCH SCORE
    # ========================================================

    jobs.sort(
        key=lambda job: job["match_score"],
        reverse=True
    )


    # ========================================================
    # RETURN TOP MATCHES
    # ========================================================

    return jobs[:8]