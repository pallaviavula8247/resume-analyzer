import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(
    nlp.vocab,
    attr="LOWER",
)

SKILLS = [

    # Languages
    "Python","Java","C","C++","JavaScript","TypeScript",

    # Frontend
    "HTML","CSS","Bootstrap","Tailwind CSS","React","Angular","Vue","Next.js",

    # Backend
    "Django","Flask","FastAPI","Node.js","Express","Spring Boot",

    # Databases
    "SQL","MySQL","PostgreSQL","MongoDB","SQLite","Oracle",

    # Cloud
    "AWS","Azure","Google Cloud",

    # DevOps
    "Git","GitHub","Docker","Kubernetes","Jenkins","CI/CD",

    # APIs
    "REST API","GraphQL",

    # AI / ML
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "OpenCV",

    # Tools
    "Linux",
    "Postman",
    "VS Code",
]

patterns = [
    nlp.make_doc(skill)
    for skill in SKILLS
]

matcher.add(
    "SKILLS",
    patterns,
)


def extract_skills(text):

    doc = nlp(text)

    matches = matcher(doc)

    skills = set()

    for _, start, end in matches:
        skills.add(doc[start:end].text)

    return sorted(skills)