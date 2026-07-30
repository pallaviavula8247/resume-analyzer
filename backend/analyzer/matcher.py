import re

# ============================================================
# Master Technical Skills Database
# ============================================================

TECH_SKILLS = [

    # Programming
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",

    # Frontend
    "HTML",
    "CSS",
    "Bootstrap",
    "Tailwind",
    "React",
    "Angular",
    "Vue",

    # Backend
    "Django",
    "Flask",
    "FastAPI",
    "Node.js",
    "Express",

    # Database
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "SQLite",
    "Oracle",

    # Version Control
    "Git",
    "GitHub",

    # Cloud
    "AWS",
    "Azure",
    "Google Cloud",

    # DevOps
    "Docker",
    "Kubernetes",
    "Jenkins",

    # AI / ML
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "OpenCV",
    "NLP",

    # Data Science
    "NumPy",
    "Pandas",
    "Matplotlib",
    "Power BI",
    "Tableau",

    # APIs
    "REST",
    "REST API",
    "GraphQL",

    # Others
    "Linux",
    "Figma",
]

# ============================================================
# Normalize Skills
# ============================================================

def normalize_skills(skills):
    """
    Convert skills into lowercase for comparison.
    """

    return list(
        set(
            skill.strip().lower()
            for skill in skills
            if skill
        )
    )


# ============================================================
# Extract Skills from Job Description
# ============================================================

def extract_job_skills(job_description):

    text = job_description.lower()

    found_skills = []

    for skill in TECH_SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


# ============================================================
# Matching Skills
# ============================================================

def get_matching_skills(resume_skills, job_skills):

    resume = normalize_skills(resume_skills)
    jobs = normalize_skills(job_skills)

    matched = []

    for skill in job_skills:

        if skill.lower() in resume:
            matched.append(skill)

    return sorted(matched)


# ============================================================
# Missing Skills
# ============================================================

def get_missing_skills(resume_skills, job_skills):

    resume = normalize_skills(resume_skills)

    missing = []

    for skill in job_skills:

        if skill.lower() not in resume:
            missing.append(skill)

    return sorted(missing)


# ============================================================
# Extra Skills
# ============================================================

def get_extra_skills(resume_skills, job_skills):

    jobs = normalize_skills(job_skills)

    extra = []

    for skill in resume_skills:

        if skill.lower() not in jobs:
            extra.append(skill)

    return sorted(list(set(extra)))


# ============================================================
# Match Score
# ============================================================

def calculate_match_score(resume_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    matched = get_matching_skills(
        resume_skills,
        job_skills,
    )

    score = (len(matched) / len(job_skills)) * 100

    return round(score, 2)


# ============================================================
# Recommendations
# ============================================================

def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        recommendations.append(
            f"Learn {skill}"
        )

    return recommendations


# ============================================================
# Resume Matching Engine
# ============================================================

def match_resume(resume_data, job_description):

    resume_skills = resume_data.get("skills", [])

    job_skills = extract_job_skills(
        job_description
    )

    matched_skills = get_matching_skills(
        resume_skills,
        job_skills,
    )

    missing_skills = get_missing_skills(
        resume_skills,
        job_skills,
    )

    extra_skills = get_extra_skills(
        resume_skills,
        job_skills,
    )

    score = calculate_match_score(
        resume_skills,
        job_skills,
    )

    if score >= 90:
        level = "Excellent"

    elif score >= 75:
        level = "Very Good"

    elif score >= 60:
        level = "Good"

    elif score >= 40:
        level = "Average"

    else:
        level = "Poor"

    recommendations = generate_recommendations(
        missing_skills
    )

    return {

        "match_score": score,

        "match_level": level,

        "required_skills": job_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "extra_skills": extra_skills,

        "recommendations": recommendations,

        "total_required_skills": len(job_skills),

        "matched_count": len(matched_skills),

        "missing_count": len(missing_skills),

        "extra_count": len(extra_skills),
    }