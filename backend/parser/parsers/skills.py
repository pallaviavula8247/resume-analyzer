"""
Skills Parser

Extracts technical skills from resume text.
"""

import re

from parser.constants import SKILLS


def extract_skills(text):
    """
    Extract skills from resume text.

    Args:
        text (str): Extracted resume text.

    Returns:
        list: List of detected skills.
    """

    if not text:
        return []

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    # Remove duplicates while preserving order
    unique_skills = list(dict.fromkeys(found_skills))

    return unique_skills