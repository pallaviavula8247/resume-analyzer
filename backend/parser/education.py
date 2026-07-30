import re

KEYWORDS = [
    "b.tech",
    "btech",
    "m.tech",
    "mtech",
    "bachelor",
    "master",
    "engineering",
    "degree",
    "college",
    "university",
    "cgpa",
]


def extract_education(text):

    education = []

    lines = text.split("\n")

    for line in lines:

        lower = line.lower()

        if any(word in lower for word in KEYWORDS):

            education.append(line.strip())

    return list(dict.fromkeys(education))