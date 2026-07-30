import re

SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "TypeScript",
    "React",
    "Angular",
    "Vue",
    "HTML",
    "CSS",
    "Bootstrap",
    "Tailwind",
    "Django",
    "Flask",
    "FastAPI",
    "Node.js",
    "Express",
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
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "OpenCV",
    "Machine Learning",
    "Deep Learning",
    "NLP",
]


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill.lower()) + r"\b", text):
            found.append(skill)

    return sorted(list(set(found)))