"""
Certification Parser
"""


CERTIFICATION_KEYWORDS = [
    "Certification",
    "Certifications",
    "Certificate",
]


def extract_certifications(text):
    """
    Extract certifications.
    """

    certifications = []

    if not text:
        return certifications

    lines = text.splitlines()

    capture = False

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if any(
            word.lower() in line.lower()
            for word in CERTIFICATION_KEYWORDS
        ):
            capture = True
            continue

        if capture:

            if line.isupper():
                break

            certifications.append(line)

    return certifications