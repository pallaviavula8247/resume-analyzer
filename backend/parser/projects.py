WORDS = [
    "project",
    "developed",
    "designed",
    "implemented",
    "built",
]


def extract_projects(text):

    projects = []

    for line in text.split("\n"):

        lower = line.lower()

        if any(word in lower for word in WORDS):

            projects.append(line.strip())

    return list(dict.fromkeys(projects))