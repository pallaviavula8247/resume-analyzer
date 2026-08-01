"""
Career recommendation service.
"""

CAREER_MAP = {
    "Python": [
        "Python Developer",
        "Backend Developer",
    ],
    "Django": [
        "Python Django Developer",
        "Backend Engineer",
    ],
    "React": [
        "Frontend Developer",
        "Full Stack Developer",
    ],
    "SQL": [
        "Database Developer",
        "Data Analyst",
    ],
    "Machine Learning": [
        "Machine Learning Engineer",
        "AI Engineer",
    ],
    "Deep Learning": [
        "AI Engineer",
    ],
    "TensorFlow": [
        "AI Engineer",
    ],
    "PyTorch": [
        "AI Engineer",
    ],
    "NumPy": [
        "Data Analyst",
        "Data Scientist",
    ],
    "Pandas": [
        "Data Analyst",
        "Data Scientist",
    ],
    "AWS": [
        "Cloud Engineer",
        "DevOps Engineer",
    ],
    "Docker": [
        "DevOps Engineer",
        "Backend Engineer",
    ],
}


def recommend_careers(skills):
    """
    Recommend career roles based on resume skills.
    """

    careers = set()

    for skill in skills:
        if skill in CAREER_MAP:
            careers.update(CAREER_MAP[skill])

    if not careers:

        careers = {
            "Software Developer",
            "Python Developer",
        }

    return sorted(list(careers))