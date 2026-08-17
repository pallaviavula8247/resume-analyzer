"""
Projects Parser

Extracts ONLY projects that appear inside the
Projects section of the resume.
"""

import re


PROJECT_HEADERS = {
    "project",
    "projects",
    "academic projects",
    "personal projects",
    "major projects",
    "minor projects",
}


NEXT_SECTION_HEADERS = {
    "experience",
    "work experience",
    "professional experience",
    "employment",
    "education",
    "skills",
    "technical skills",
    "certifications",
    "certification",
    "languages",
    "achievements",
    "strengths",
    "declaration",
    "interests",
    "references",
}


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


def normalize_header(text):
    """
    Normalize a section heading.

    Handles PDF extraction such as:

    Academic Projects
    academicprojects
    ACADEMIC PROJECTS
    """

    if not text:
        return ""

    return re.sub(
        r"[^a-z]",
        "",
        text.lower(),
    )


NORMALIZED_PROJECT_HEADERS = {
    normalize_header(header)
    for header in PROJECT_HEADERS
}


NORMALIZED_NEXT_HEADERS = {
    normalize_header(header)
    for header in NEXT_SECTION_HEADERS
}


def is_project_header(line):
    normalized = normalize_header(line)

    return normalized in NORMALIZED_PROJECT_HEADERS


def is_next_section(line):
    normalized = normalize_header(line)

    return normalized in NORMALIZED_NEXT_HEADERS


def is_probable_project_name(line):
    """
    Determine whether a line looks like a project title.

    We intentionally DO NOT treat every short line
    as a project.
    """

    line = line.strip()

    if not line:
        return False

    if is_next_section(line):
        return False

    if line in {"•", "-", "*", "o"}:
        return False

    # Ignore obvious bullet-only prefixes
    line = re.sub(
        r"^[•\-\*\u2022]\s*",
        "",
        line,
    ).strip()

    if len(line) < 4:
        return False

    if len(line) > 150:
        return False

    # These are clearly not project names
    blocked = [
        "declaration",
        "strengths",
        "certification",
        "certifications",
        "languages",
    ]

    normalized = normalize_header(line)

    if normalized in {
        normalize_header(item)
        for item in blocked
    }:
        return False

    return True


def extract_technologies(text):
    """
    Extract technologies from a project description.
    """

    technologies = []

    lower_text = text.lower()

    for technology in TECHNOLOGIES:

        if technology.lower() in lower_text:

            if technology not in technologies:
                technologies.append(technology)

    return technologies


def extract_projects(text):
    """
    Extract projects ONLY from the Projects section.
    """

    if not text:
        return []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    projects = []

    inside_projects = False
    current = None

    for line in lines:

        # --------------------------------------------------
        # START PROJECT SECTION
        # --------------------------------------------------

        if is_project_header(line):

            inside_projects = True
            continue

        # --------------------------------------------------
        # STOP PROJECT SECTION
        # --------------------------------------------------

        if inside_projects and is_next_section(line):

            if current:
                projects.append(current)

            current = None
            break

        if not inside_projects:
            continue

        # --------------------------------------------------
        # REMOVE BULLET
        # --------------------------------------------------

        clean_line = re.sub(
            r"^[•\-\*\u2022]\s*",
            "",
            line,
        ).strip()

        if not clean_line:
            continue

        # --------------------------------------------------
        # PROJECT NAME
        # --------------------------------------------------

        if is_probable_project_name(clean_line):

            # If there is already a project,
            # this line can start another project.
            if current:

                projects.append(current)

            current = {
                "project_name": clean_line,
                "technologies": [],
                "description": "",
            }

            continue

        # --------------------------------------------------
        # DESCRIPTION
        # --------------------------------------------------

        if current:

            if current["description"]:
                current["description"] += " "

            current["description"] += clean_line

    # ------------------------------------------------------
    # SAVE LAST PROJECT
    # ------------------------------------------------------

    if current:
        projects.append(current)

    # ------------------------------------------------------
    # CLEAN PROJECTS
    # ------------------------------------------------------

    cleaned = []
    seen = set()

    for project in projects:

        name = project["project_name"].strip()

        if not name:
            continue

        normalized_name = name.lower()

        if normalized_name in seen:
            continue

        seen.add(normalized_name)

        # Extract technologies from name + description
        combined_text = (
            project["project_name"]
            + " "
            + project["description"]
        )

        project["technologies"] = extract_technologies(
            combined_text
        )

        cleaned.append(project)

    return cleaned