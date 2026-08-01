"""
Personal Information Parser

Extract:
- Full Name
- Email
- Phone
- Location
- LinkedIn
- GitHub
- Portfolio
"""

import re

from parser.nlp import nlp


EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

PHONE_PATTERN = re.compile(
    r"(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{3,5}\)?[\s-]?)?\d{10}"
)

LINKEDIN_PATTERN = re.compile(
    r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",
    re.IGNORECASE,
)

GITHUB_PATTERN = re.compile(
    r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+",
    re.IGNORECASE,
)

URL_PATTERN = re.compile(
    r"https?://[^\s]+",
    re.IGNORECASE,
)


IGNORE_LINES = {
    "resume",
    "curriculum vitae",
    "cv",
    "india",
    "andhra pradesh",
    "telangana",
}


def is_possible_name(line):
    """
    Check whether a line is likely to be a person's name.
    """

    line = line.strip()

    if len(line) < 3:
        return False

    if len(line.split()) > 4:
        return False

    if any(char.isdigit() for char in line):
        return False

    if "@" in line:
        return False

    if "http" in line.lower():
        return False

    if line.lower() in IGNORE_LINES:
        return False

    words = line.split()

    return all(word[0].isupper() for word in words if word)


def extract_personal_info(text):
    """
    Extract personal information.
    """

    result = {
        "full_name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": "",
        "portfolio": "",
    }

    if not text:
        return result

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # -------------------------------
    # Name from first few lines
    # -------------------------------

    for line in lines[:8]:

        if is_possible_name(line):
            result["full_name"] = line
            break

    # -------------------------------
    # spaCy fallback
    # -------------------------------

    if not result["full_name"]:

        doc = nlp(text)

        for ent in doc.ents:

            if ent.label_ == "PERSON":

                if len(ent.text.split()) >= 2:
                    result["full_name"] = ent.text
                    break

    # -------------------------------
    # Location
    # -------------------------------

    doc = nlp(text)

    locations = []

    for ent in doc.ents:

        if ent.label_ in ("GPE", "LOC"):

            if ent.text not in locations:
                locations.append(ent.text)

    if locations:
        result["location"] = ", ".join(locations)

    # -------------------------------
    # Email
    # -------------------------------

    email = EMAIL_PATTERN.search(text)

    if email:
        result["email"] = email.group()

    # -------------------------------
    # Phone
    # -------------------------------

    phone = PHONE_PATTERN.search(text)

    if phone:
        result["phone"] = phone.group()

    # -------------------------------
    # LinkedIn
    # -------------------------------

    linkedin = LINKEDIN_PATTERN.search(text)

    if linkedin:

        url = linkedin.group()

        if not url.startswith("http"):
            url = "https://" + url

        result["linkedin"] = url

    # -------------------------------
    # GitHub
    # -------------------------------

    github = GITHUB_PATTERN.search(text)

    if github:

        url = github.group()

        if not url.startswith("http"):
            url = "https://" + url

        result["github"] = url

    # -------------------------------
    # Portfolio
    # -------------------------------

    urls = URL_PATTERN.findall(text)

    for url in urls:

        lower = url.lower()

        if "linkedin" in lower:
            continue

        if "github" in lower:
            continue

        result["portfolio"] = url
        break

    return result