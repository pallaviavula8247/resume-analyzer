"""
Certification Parser

Extracts certifications ONLY from the
Certification section of the resume.
"""

import re


CERTIFICATION_HEADERS = {
    "certification",
    "certifications",
    "certificates",
    "professional certifications",
}


NEXT_SECTION_HEADERS = {
    "experience",
    "work experience",
    "professional experience",
    "education",
    "skills",
    "technical skills",
    "projects",
    "project",
    "languages",
    "achievements",
    "strengths",
    "declaration",
    "interests",
    "references",
}


def normalize_header(text):
    if not text:
        return ""

    return re.sub(
        r"[^a-z]",
        "",
        text.lower(),
    )


NORMALIZED_CERT_HEADERS = {
    normalize_header(item)
    for item in CERTIFICATION_HEADERS
}


NORMALIZED_NEXT_HEADERS = {
    normalize_header(item)
    for item in NEXT_SECTION_HEADERS
}


def extract_certifications(text):
    """
    Extract certifications only from the actual
    certification section.
    """

    if not text:
        return []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    certifications = []

    inside_certifications = False
    current = ""

    for line in lines:

        normalized = normalize_header(line)

        # --------------------------------------------------
        # START CERTIFICATION SECTION
        # --------------------------------------------------

        if normalized in NORMALIZED_CERT_HEADERS:

            inside_certifications = True
            continue

        if not inside_certifications:
            continue

        # --------------------------------------------------
        # STOP CERTIFICATION SECTION
        # --------------------------------------------------

        if normalized in NORMALIZED_NEXT_HEADERS:

            if current:
                certifications.append(
                    current.strip()
                )

            break

        # --------------------------------------------------
        # IGNORE BULLETS
        # --------------------------------------------------

        line = re.sub(
            r"^[•\-\*\u2022]\s*",
            "",
            line,
        ).strip()

        if not line:
            continue

        # --------------------------------------------------
        # APPEND CERTIFICATION TEXT
        # --------------------------------------------------

        if current:
            current += " " + line
        else:
            current = line

    # ------------------------------------------------------
    # SAVE LAST CERTIFICATION
    # ------------------------------------------------------

    if current:
        certifications.append(
            current.strip()
        )

    # ------------------------------------------------------
    # CLEAN
    # ------------------------------------------------------

    cleaned = []

    for item in certifications:

        if item and item not in cleaned:
            cleaned.append(item)

    return cleaned