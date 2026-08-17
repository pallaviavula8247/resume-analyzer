"""
Skills Parser

Extracts technical skills ONLY from the actual resume.

Important:
- No default skills are added.
- Skills must actually occur in the resume.
- Skills section is preferred.
- Certification/project occurrences are not treated as skills
  when a proper Skills section is available.
"""

import re

from parser.constants import SKILLS


# ============================================================
# SKILL ALIASES
# ============================================================

SKILL_ALIASES = {
    "Python": ["python"],
    "Java": [r"\bjava\b"],
    "C": [
        r"\bc\s*\(beginner\)",
        r"\bc programming\b",
        r"\bc language\b",
        r"(?<![a-z])c(?![a-z+#])",
    ],
    "C++": [r"c\+\+"],
    "JavaScript": ["javascript", "java script"],
    "TypeScript": ["typescript"],
    "HTML": [r"\bhtml5?\b"],
    "CSS": [r"\bcss3?\b"],
    "React": ["react", "react.js", "reactjs"],
    "Angular": ["angular"],
    "Vue": ["vue", "vue.js", "vuejs"],
    "Node.js": ["node.js", "nodejs", "node js"],
    "Express": ["express", "express.js", "expressjs"],
    "Django": ["django"],
    "Flask": ["flask"],
    "FastAPI": ["fastapi", "fast api"],
    "SQL": [r"\bsql\b"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "SQLite": ["sqlite"],
    "MongoDB": ["mongodb", "mongo db"],
    "Oracle": ["oracle database", "oracle db"],
    "Git": [r"\bgit\b"],
    "GitHub": ["github", "git hub"],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "Machine Learning": [
        "machine learning",
        "machinelearning",
    ],
    "Deep Learning": [
        "deep learning",
        "deeplearning",
    ],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch", "py torch"],
    "OpenCV": ["opencv", "open cv"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy", "num py"],
    "Scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn",
    ],
    "REST API": [
        "rest api",
        "restful api",
        "restful apis",
    ],
    "Matplotlib": ["matplotlib"],
    "Jupyter Notebook": [
        "jupyter notebook",
        "jupyter",
    ],
    "Visual Studio Code": [
        "visual studio code",
        "visualstudiocode",
        "visual studio code",
        "vs code",
        "vscode",
    ],
}


# ============================================================
# SECTION NAMES
# ============================================================

SKILLS_HEADERS = [
    "skills",
    "technical skills",
    "technical skills and tools",
    "technical skills & tools",
    "skills and technologies",
    "skills & technologies",
]

STOP_HEADERS = [
    "projects",
    "academic projects",
    "personal projects",
    "experience",
    "work experience",
    "professional experience",
    "education",
    "certification",
    "certifications",
    "languages",
    "achievements",
    "strengths",
    "declaration",
    "declaration:-",
    "references",
]


# ============================================================
# NORMALIZE HEADER
# ============================================================

def normalize_header(line):
    """
    Normalize a line so PDF formatting differences don't
    prevent section detection.
    """

    line = line.lower().strip()

    # Remove bullets
    line = line.replace("•", "")

    # Remove punctuation
    line = re.sub(
        r"[^a-z0-9& ]",
        "",
        line,
    )

    # Remove repeated spaces
    line = re.sub(
        r"\s+",
        " ",
        line,
    )

    return line.strip()


# ============================================================
# FIND SKILLS SECTION
# ============================================================

def extract_skills_section(text):
    """
    Extract content belonging to the Skills section.

    Handles PDF formatting where:
        SKILLS
        Programming Libraries/Frameworks
        ...

    may be separated into multiple lines.
    """

    if not text:
        return ""

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    inside_skills = False
    skills_lines = []

    for line in lines:

        normalized = normalize_header(line)

        # ----------------------------------------------------
        # START
        # ----------------------------------------------------

        if normalized in SKILLS_HEADERS:

            inside_skills = True
            continue

        # ----------------------------------------------------
        # STOP
        # ----------------------------------------------------

        if inside_skills:

            if normalized in STOP_HEADERS:

                break

            skills_lines.append(line)

    return "\n".join(skills_lines)


# ============================================================
# CHECK SKILL
# ============================================================

def contains_skill(text, patterns):
    """
    Check whether a skill occurs in text.
    """

    text = text.lower()

    for pattern in patterns:

        try:

            if re.search(
                pattern,
                text,
                re.IGNORECASE,
            ):
                return True

        except re.error:

            if pattern.lower() in text:
                return True

    return False


# ============================================================
# MAIN FUNCTION
# ============================================================

def extract_skills(text):
    """
    Extract technical skills from the uploaded resume.

    The resume itself is the source of truth.

    If a Skills section exists:
        search ONLY inside that section.

    If no Skills section exists:
        search the full resume.
    """

    if not text:
        return []

    # --------------------------------------------------------
    # Get Skills Section
    # --------------------------------------------------------

    skills_section = extract_skills_section(text)

    # --------------------------------------------------------
    # IMPORTANT
    #
    # If a Skills section exists, NEVER search the whole
    # resume.
    #
    # This prevents:
    #
    # Certification:
    # AWS
    #
    # from becoming a resume skill.
    # --------------------------------------------------------

    if skills_section.strip():

        search_text = skills_section

    else:

        search_text = text

    # --------------------------------------------------------
    # Detect Skills
    # --------------------------------------------------------

    found_skills = []

    for skill in SKILLS:

        patterns = SKILL_ALIASES.get(
            skill,
            [re.escape(skill.lower())],
        )

        if contains_skill(
            search_text,
            patterns,
        ):

            found_skills.append(skill)

    # --------------------------------------------------------
    # Remove duplicates
    # --------------------------------------------------------

    return list(
        dict.fromkeys(
            found_skills
        )
    )