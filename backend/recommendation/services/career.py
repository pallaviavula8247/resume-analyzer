"""
career.py

AI Career Recommendation Service

This module recommends suitable career roles
based on the candidate's skills.
"""

from collections import Counter


# ----------------------------------------
# Career Mapping
# ----------------------------------------

CAREER_MAP = {

    "Python": [
        "Python Developer",
        "Backend Developer",
        "Software Engineer",
    ],

    "Django": [
        "Python Django Developer",
        "Backend Developer",
        "Full Stack Developer",
    ],

    "Flask": [
        "Python Developer",
        "Backend Developer",
    ],

    "React": [
        "Frontend Developer",
        "Full Stack Developer",
    ],

    "Angular": [
        "Frontend Developer",
        "Full Stack Developer",
    ],

    "JavaScript": [
        "Frontend Developer",
        "Web Developer",
    ],

    "HTML": [
        "Frontend Developer",
    ],

    "CSS": [
        "Frontend Developer",
    ],

    "SQL": [
        "Database Developer",
        "Data Analyst",
        "Backend Developer",
    ],

    "MySQL": [
        "Database Developer",
    ],

    "PostgreSQL": [
        "Backend Developer",
    ],

    "MongoDB": [
        "Backend Developer",
        "Full Stack Developer",
    ],

    "Git": [
        "Software Engineer",
    ],

    "GitHub": [
        "Software Engineer",
    ],

    "Docker": [
        "DevOps Engineer",
        "Backend Developer",
    ],

    "Kubernetes": [
        "DevOps Engineer",
    ],

    "AWS": [
        "Cloud Engineer",
        "DevOps Engineer",
    ],

    "Azure": [
        "Cloud Engineer",
    ],

    "GCP": [
        "Cloud Engineer",
    ],

    "Machine Learning": [
        "Machine Learning Engineer",
        "AI Engineer",
        "Data Scientist",
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

    "OpenCV": [
        "Computer Vision Engineer",
    ],

    "NLP": [
        "NLP Engineer",
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

    "Matplotlib": [
        "Data Analyst",
    ],

    "Power BI": [
        "Business Intelligence Analyst",
        "Data Analyst",
    ],

    "Excel": [
        "Data Analyst",
    ],

    "REST API": [
        "Backend Developer",
        "Full Stack Developer",
    ],
}


# ----------------------------------------
# Career Recommendation
# ----------------------------------------

def recommend_careers(skills):
    """
    Recommend career roles based on resume skills.

    Parameters
    ----------
    skills : list

    Returns
    -------
    list
    """

    if not skills:
        return [
            "Software Developer",
            "Python Developer",
        ]

    counter = Counter()

    for skill in skills:

        skill = skill.strip()

        if skill in CAREER_MAP:

            for role in CAREER_MAP[skill]:

                counter[role] += 1

    if not counter:

        return [
            "Software Developer",
            "Python Developer",
        ]

    recommendations = [
        role
        for role, _
        in counter.most_common(6)
    ]

    return recommendations


# ----------------------------------------
# Testing
# ----------------------------------------

if __name__ == "__main__":

    skills = [
        "Python",
        "Django",
        "AWS",
        "NumPy",
        "Pandas",
    ]

    print(recommend_careers(skills))