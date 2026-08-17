"""
Skills Parser

Extracts technical skills ONLY from the Skills section
when a Skills section exists.

The resume is the source of truth.
"""

import re

from parser.constants import SKILLS


# ============================================================
# SKILL ALIASES
# ============================================================

SKILL_ALIASES = {
    "Python": ["python"],

    "C": [
        r"\bc\s*\(beginner\)",
        r"\bc programming\b",
        r"\bc language\b",
        r"(?<![a-z])c(?![a-z+#])",
    ],

    "C++": [r"c\+\+"],

    "Java": [r"\bjava\b"],

    "JavaScript": [
        "javascript",
        "java script",
    ],

    "TypeScript": ["typescript"],

    "HTML": [r"\bhtml5?\b"],

    "CSS": [r"\bcss3?\b"],

    "React": [
        "react",
        "react.js",
        "reactjs",
    ],

    "Angular": ["angular"],

    "Vue": [
        "vue",
        "vue.js",
        "vuejs",
    ],

    "Node.js": [
        "node.js",
        "nodejs",
        "node js",
    ],

    "Express": [
        "express",
        "express.js",
        "expressjs",
    ],

    "Django": ["django"],
    "Flask": ["flask"],

    "FastAPI": [
        "fastapi",
        "fast api",
    ],

    "SQL": [r"\bsql\b"],
    "MySQL": ["mysql"],

    "PostgreSQL": [
        "postgresql",
        "postgres",
    ],

    "SQLite": ["sqlite"],

    "MongoDB": [
        "mongodb",
        "mongo db",
    ],

    "Oracle": [
        "oracle database",
        "oracle db",
    ],

    "Git": [r"\bgit\b"],

    "GitHub": [
        "github",
        "git hub",
    ],

    "Docker": ["docker"],
    "Kubernetes": ["kubernetes"],

    "AWS": [
        "aws",
        "amazon web services",
    ],

    "Azure": [
        "azure",
        "microsoft azure",
    ],

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

    "OpenCV": [
        "opencv",
        "open cv",
    ],

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
        "vs code",
        "vscode",
    ],
}


# ============================================================
# SECTION HEADERS
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
    Normalize section header text.
    """

    line = line.lower().strip()

    line = line.replace("•", "")

    line = re.sub(
        r"[^a-z0-9& ]",
        "",
        line,
    )

    line = re.sub(
        r"\s+",
        " ",
        line,
    )

    return line.strip()


# ============================================================
# EXTRACT SKILLS SECTION
# ============================================================

def extract_skills_section(text):
    """
    Extract only the text belonging to the Skills section.
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

        # Start Skills section
        if normalized in SKILLS_HEADERS:

            inside_skills = True

            continue

        # Stop Skills section
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
    Check whether a skill exists in the supplied text.
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
# MAIN SKILL EXTRACTION
# ============================================================

def extract_skills(text):
    """
    Extract skills from the actual resume.

    If a Skills section exists:
        search ONLY that section.

    Otherwise:
        search the complete resume.
    """

    if not text:
        return []

    skills_section = extract_skills_section(text)

    if skills_section.strip():

        search_text = skills_section

    else:

        search_text = text

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

    return list(
        dict.fromkeys(found_skills)
    )