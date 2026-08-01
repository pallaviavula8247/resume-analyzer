"""
Education Parser

Extracts:
- Degree
- Institution
- Graduation Year
- CGPA / Percentage
"""

import re

from parser.nlp import nlp


DEGREE_KEYWORDS = [
    "Bachelor of Technology",
    "B.Tech",
    "Bachelor of Engineering",
    "B.E",
    "Bachelor of Science",
    "B.Sc",
    "Bachelor of Computer Applications",
    "BCA",

    "Master of Technology",
    "M.Tech",
    "Master of Engineering",
    "M.E",
    "Master of Science",
    "M.Sc",
    "Master of Computer Applications",
    "MCA",
    "MBA",

    "Intermediate",
    "Diploma",
    "SSC",
    "High School",
    "PhD",
]


SECTION_HEADERS = [
    "experience",
    "projects",
    "skills",
    "certifications",
    "languages",
    "achievements",
]


def extract_education(text):
    """
    Extract education details.
    """

    if not text:
        return []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    education = []
    current = None

    for line in lines:

        lower = line.lower()

        # Stop when another section starts
        if any(header in lower for header in SECTION_HEADERS):
            current = None
            continue

        # --------------------------
        # Degree
        # --------------------------

        degree_found = None

        for degree in DEGREE_KEYWORDS:

            if degree.lower() in lower:
                degree_found = degree
                break

        if degree_found:

            if current:
                education.append(current)

            current = {
                "degree": degree_found,
                "institution": "",
                "year": "",
                "score": "",
            }

            continue

        if current is None:
            continue

        # --------------------------
        # Institution
        # --------------------------

        if current["institution"] == "":

            doc = nlp(line)

            for ent in doc.ents:

                if ent.label_ == "ORG":

                    current["institution"] = ent.text
                    break

            if current["institution"] == "":

                keywords = [
                    "college",
                    "university",
                    "institute",
                    "school",
                    "academy",
                ]

                if any(word in lower for word in keywords):
                    current["institution"] = line

        # --------------------------
        # Graduation Year
        # --------------------------

        years = re.findall(
            r"(19\d{2}|20\d{2})",
            line,
        )

        if years:
            current["year"] = years[-1]

        # --------------------------
        # CGPA
        # --------------------------

        cgpa = re.search(
            r"(?:CGPA|GPA)?[: ]*([0-9]\.[0-9]{1,2})",
            line,
            re.IGNORECASE,
        )

        if cgpa:
            current["score"] = cgpa.group(1)

        # --------------------------
        # Percentage
        # --------------------------

        percentage = re.search(
            r"([0-9]{1,3}(?:\.[0-9]+)?)%",
            line,
        )

        if percentage:
            current["score"] = percentage.group(1) + "%"

    if current:
        education.append(current)

    # --------------------------
    # Remove duplicates
    # --------------------------

    unique = []

    seen = set()

    for item in education:

        key = (
            item["degree"],
            item["institution"],
            item["year"],
        )

        if key not in seen:

            seen.add(key)
            unique.append(item)

    return unique