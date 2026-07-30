import re

WORDS = [
    "intern",
    "internship",
    "developer",
    "engineer",
    "experience",
    "software",
    "worked",
    "company",
]


def extract_experience(text):

    experience = []

    for line in text.split("\n"):

        lower = line.lower()

        if any(word in lower for word in WORDS):

            experience.append(line.strip())

    return list(dict.fromkeys(experience))