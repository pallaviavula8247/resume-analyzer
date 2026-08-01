"""
Experience Parser

Extracts:
- Job Title
- Company
- Duration
- Description
"""

import re

from parser.nlp import nlp


EXPERIENCE_HEADERS = [
    "experience",
    "work experience",
    "professional experience",
    "employment",
    "internship",
    "internships",
]


NEXT_SECTIONS = [
    "education",
    "projects",
    "skills",
    "certifications",
    "languages",
    "achievements",
    "references",
]


JOB_TITLES = [
    "Software Engineer",
    "Python Developer",
    "Full Stack Developer",
    "Frontend Developer",
    "Backend Developer",
    "Web Developer",
    "Machine Learning Engineer",
    "AI Engineer",
    "Data Scientist",
    "Data Analyst",
    "Intern",
    "Trainee",
    "Research Assistant",
]


def extract_experience(text):
    """
    Extract work experience from resume.
    """

    if not text:
        return []

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    experience = []

    inside_section = False
    current = None

    for line in lines:

        lower = line.lower()

        # ----------------------------
        # Experience Section Start
        # ----------------------------

        if any(header == lower for header in EXPERIENCE_HEADERS):
            inside_section = True
            continue

        # ----------------------------
        # Stop at Next Section
        # ----------------------------

        if inside_section:

            if any(section == lower for section in NEXT_SECTIONS):

                if current:
                    experience.append(current)

                break

        if not inside_section:
            continue

        # ----------------------------
        # Job Title
        # ----------------------------

        title_found = None

        for title in JOB_TITLES:

            if title.lower() in lower:
                title_found = title
                break

        if title_found:

            if current:
                experience.append(current)

            current = {
                "job_title": title_found,
                "company": "",
                "duration": "",
                "description": "",
            }

            continue

        if current is None:
            continue

        # ----------------------------
        # Company
        # ----------------------------

        if current["company"] == "":

            doc = nlp(line)

            for ent in doc.ents:

                if ent.label_ == "ORG":

                    current["company"] = ent.text
                    break

        # ----------------------------
        # Duration
        # ----------------------------

        duration = re.search(
            r"((19|20)\d{2}\s*[-–]\s*((19|20)\d{2}|Present))",
            line,
            re.IGNORECASE,
        )

        if duration:

            current["duration"] = duration.group(1)

            continue

        # ----------------------------
        # Description
        # ----------------------------

        if (
            len(line) > 10
            and current["description"] == ""
        ):

            current["description"] = line

        elif len(line) > 10:

            current["description"] += " " + line

    if current:
        experience.append(current)

    # ----------------------------
    # Remove duplicates
    # ----------------------------

    unique = []

    seen = set()

    for item in experience:

        key = (
            item["job_title"],
            item["company"],
            item["duration"],
        )

        if key not in seen:

            seen.add(key)
            unique.append(item)

    return unique