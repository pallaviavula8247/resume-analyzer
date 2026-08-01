"""
Resume Skill Similarity Calculator
"""


# Common aliases for technical skills
SKILL_ALIASES = {
    "github": "git",
    "gitlab": "git",
    "bitbucket": "git",

    "rest": "rest api",
    "restful api": "rest api",

    "js": "javascript",
    "node": "node.js",

    "postgres": "postgresql",
    "mongo": "mongodb",

    "py": "python",

    "ml": "machine learning",
    "dl": "deep learning",

    "tf": "tensorflow",
    "sklearn": "scikit-learn",
}


def normalize_skill(skill):
    """
    Normalize a skill name.
    """

    skill = skill.strip().lower()

    return SKILL_ALIASES.get(
        skill,
        skill,
    )


def compare_skills(resume_skills, job_skills):
    """
    Compare resume skills with job skills.
    """

    resume_set = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    job_set = {
        normalize_skill(skill)
        for skill in job_skills
    }

    matched = resume_set & job_set

    missing = job_set - resume_set

    extra = resume_set - job_set

    if len(job_set) == 0:
        score = 0
    else:
        score = round(
            (len(matched) / len(job_set)) * 100,
            2,
        )

    if score >= 80:
        level = "Excellent"
    elif score >= 60:
        level = "Good"
    elif score >= 40:
        level = "Average"
    else:
        level = "Poor"

    return {
        "match_score": score,
        "match_level": level,

        "required_skills": sorted(job_set),

        "matched_skills": sorted(matched),

        "missing_skills": sorted(missing),

        "extra_skills": sorted(extra),

        "total_required_skills": len(job_set),

        "matched_count": len(matched),

        "missing_count": len(missing),

        "extra_count": len(extra),
    }