"""
Projects Parser

Extracts:
- Project Name
- Technologies
- Description
"""

import re


PROJECT_HEADERS = [
    "projects",
    "project",
    "academic projects",
    "personal projects",
    "major projects",
    "minor projects",
]


NEXT_SECTIONS = [
    "experience",
    "education",
    "skills",
    "certifications",
    "languages",
    "achievements",
    "interests",
    "references",
]


TECHNOLOGIES = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "TypeScript",
    "React",
    "ReactJS",
    "Node.js",
    "NodeJS",
    "Express",
    "Django",
    "Flask",
    "FastAPI",
    "HTML",
    "CSS",
    "Bootstrap",
    "Tailwind",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "SQLite",
    "AWS",
    "Docker",
    "Git",
    "GitHub",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
]


def extract_projects(text):
    """
    Extract projects from resume.
    """

    if not text:
        return []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    projects = []

    inside_section = False

    current = None

    for line in lines:

        lower = line.lower()

        # -----------------------------
        # Project Section Start
        # -----------------------------

        if any(header == lower for header in PROJECT_HEADERS):

            inside_section = True
            continue

        # -----------------------------
        # End Section
        # -----------------------------

        if inside_section:

            if any(section == lower for section in NEXT_SECTIONS):

                if current:
                    projects.append(current)

                break

        if not inside_section:
            continue

        # -----------------------------
        # Ignore Bullet Only
        # -----------------------------

        if line in [
            "•",
            "-",
            "*",
            "o",
        ]:
            continue

        # -----------------------------
        # New Project
        # -----------------------------

        if (
            len(line) <= 80
            and not line.endswith(".")
        ):

            if current:
                projects.append(current)

            current = {
                "project_name": line,
                "technologies": [],
                "description": "",
            }

            continue

        if current is None:
            continue

        # -----------------------------
        # Technologies
        # -----------------------------

        for tech in TECHNOLOGIES:

            if tech.lower() in line.lower():

                if tech not in current["technologies"]:

                    current["technologies"].append(
                        tech
                    )

        # -----------------------------
        # Description
        # -----------------------------

        if current["description"]:

            current["description"] += " "

        current["description"] += line

    if current:
        projects.append(current)

    # -----------------------------
    # Remove Empty Projects
    # -----------------------------

    clean_projects = []

    seen = set()

    for project in projects:

        if len(project["project_name"]) < 2:
            continue

        key = project["project_name"].lower()

        if key in seen:
            continue

        seen.add(key)

        clean_projects.append(project)

    return clean_projects