WORDS = [
    "certificate",
    "certification",
    "certified",
    "course",
    "coursera",
    "udemy",
    "nptel",
    "aicte",
]


def extract_certifications(text):

    certificates = []

    for line in text.split("\n"):

        lower = line.lower()

        if any(word in lower for word in WORDS):

            certificates.append(line.strip())

    return list(dict.fromkeys(certificates))