"""
Education Parser

Extracts education information directly from
the education section of the resume.
"""

import re


EDUCATION_HEADERS = {
    "education",
    "academic background",
    "educational qualifications",
    "academic qualifications",
}


NEXT_SECTION_HEADERS = {
    "experience",
    "work experience",
    "professional experience",
    "employment",
    "internship",
    "internships",
    "projects",
    "project",
    "skills",
    "technical skills",
    "certifications",
    "certification",
    "languages",
    "achievements",
    "strengths",
    "references",
    "declaration",
}


def normalize(text):
    """
    Normalize PDF text for matching.
    """

    if not text:
        return ""

    return re.sub(
        r"[^a-z0-9]",
        "",
        text.lower(),
    )


def is_education_header(line):
    return normalize(line) in {
        normalize(item)
        for item in EDUCATION_HEADERS
    }


def is_next_section(line):
    return normalize(line) in {
        normalize(item)
        for item in NEXT_SECTION_HEADERS
    }


def detect_degree(text):
    """
    Detect the actual degree appearing in the text.
    """

    normalized = normalize(text)

    degree_patterns = [
        (
            "Bachelor of Technology",
            [
                "btech",
                "bacheloroftechnology",
            ],
        ),
        (
            "Bachelor of Engineering",
            [
                "be",
                "bachelorofengineering",
            ],
        ),
        (
            "Bachelor of Science",
            [
                "bsc",
                "bachelorofscience",
            ],
        ),
        (
            "Bachelor of Computer Applications",
            [
                "bca",
                "bachelorofcomputerapplications",
            ],
        ),
        (
            "Master of Technology",
            [
                "mtech",
                "masteroftechnology",
            ],
        ),
        (
            "Master of Engineering",
            [
                "me",
                "masterofengineering",
            ],
        ),
        (
            "Master of Science",
            [
                "msc",
                "masterofscience",
            ],
        ),
        (
            "Master of Computer Applications",
            [
                "mca",
                "masterofcomputerapplications",
            ],
        ),
        (
            "MBA",
            [
                "mba",
                "masterofbusinessadministration",
            ],
        ),
        (
            "Intermediate",
            [
                "intermediate",
            ],
        ),
        (
            "Diploma",
            [
                "diploma",
            ],
        ),
        (
            "Secondary School Certificate",
            [
                "ssc",
                "secondaryschoolcertificate",
            ],
        ),
        (
            "High School",
            [
                "highschool",
            ],
        ),
        (
            "PhD",
            [
                "phd",
                "doctorofphilosophy",
            ],
        ),
    ]

    for degree_name, patterns in degree_patterns:

        for pattern in patterns:

            if pattern in normalized:

                return degree_name

    return None


def extract_years(text):
    """
    Extract years such as:
    2023
    2023 - 2027
    """

    return re.findall(
        r"\b(?:19|20)\d{2}\b",
        text,
    )


def extract_score(text):
    """
    Extract CGPA or percentage.
    """

    cgpa = re.search(
        r"(?:cgpa|gpa)\s*[:\-]?\s*([0-9]+(?:\.[0-9]+)?)",
        text,
        re.IGNORECASE,
    )

    if cgpa:
        return cgpa.group(1)

    percentage = re.search(
        r"([0-9]+(?:\.[0-9]+)?)\s*%",
        text,
    )

    if percentage:
        return percentage.group(1) + "%"

    return ""


def extract_institution(text):
    """
    Try to extract the institution from an education entry.
    """

    institution_patterns = [
        r"(Annamacharya Institute of TechnologyandSciences)",
        r"(Govt\s*Junior\s*College)",
        r"(ZPH\s*high\s*School)",
        r"([A-Za-z ]+(?:University|College|Institute|School))",
    ]

    for pattern in institution_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

    return ""


def extract_education(text):
    """
    Extract all education entries appearing
    in the resume.
    """

    if not text:
        return []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    education = []

    inside_education = False
    current = None

    for line in lines:

        # --------------------------------------------------
        # START EDUCATION
        # --------------------------------------------------

        if is_education_header(line):

            inside_education = True
            continue

        if not inside_education:
            continue

        # --------------------------------------------------
        # STOP EDUCATION
        # --------------------------------------------------

        if is_next_section(line):

            if current:
                education.append(current)

            current = None
            break

        # --------------------------------------------------
        # CHECK DEGREE
        # --------------------------------------------------

        degree = detect_degree(line)

        if degree:

            if current:
                education.append(current)

            current = {
                "degree": degree,
                "institution": "",
                "year": "",
                "score": "",
            }

        # --------------------------------------------------
        # IF NO CURRENT ENTRY
        # --------------------------------------------------

        if current is None:
            continue

        # --------------------------------------------------
        # INSTITUTION
        # --------------------------------------------------

        if not current["institution"]:

            institution = extract_institution(line)

            if institution:
                current["institution"] = institution

        # --------------------------------------------------
        # YEARS
        # --------------------------------------------------

        years = extract_years(line)

        if years:

            if len(years) >= 2:
                current["year"] = (
                    f"{years[0]} - {years[1]}"
                )
            else:
                current["year"] = years[0]

        # --------------------------------------------------
        # SCORE
        # --------------------------------------------------

        score = extract_score(line)

        if score:
            current["score"] = score

    # ------------------------------------------------------
    # SAVE LAST
    # ------------------------------------------------------

    if current:
        education.append(current)

    # ------------------------------------------------------
    # REMOVE DUPLICATES
    # ------------------------------------------------------

    unique = []
    seen = set()

    for item in education:

        key = (
            item["degree"],
            item["institution"],
            item["year"],
            item["score"],
        )

        if key not in seen:

            seen.add(key)
            unique.append(item)

    return unique