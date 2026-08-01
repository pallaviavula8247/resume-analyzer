import re


# Common technical skills for ATS matching
DEFAULT_SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "TypeScript",
    "React",
    "Angular",
    "Vue",
    "Node.js",
    "Django",
    "Flask",
    "FastAPI",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "SQLite",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "GCP",
    "HTML",
    "CSS",
    "REST API",
    "GraphQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "NumPy",
    "Pandas",
    "Scikit-learn",
    "OpenCV",
]


def extract_keywords(job_description):
    """
    Extract relevant skills from a job description.
    """

    if not job_description:
        return []

    text = job_description.lower()

    keywords = []

    for skill in DEFAULT_SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            keywords.append(skill)

    return sorted(list(set(keywords)))


def compare_keywords(resume_skills, job_keywords):
    """
    Compare resume skills with job keywords.
    """

    resume_set = {skill.lower() for skill in resume_skills}
    keyword_set = {skill.lower() for skill in job_keywords}

    matched = sorted(
        list(resume_set & keyword_set)
    )

    missing = sorted(
        list(keyword_set - resume_set)
    )

    extra = sorted(
        list(resume_set - keyword_set)
    )

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
        "matched_count": len(matched),
        "missing_count": len(missing),
        "extra_count": len(extra),
    }