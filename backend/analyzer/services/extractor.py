"""
AI Job Skill Extractor
"""

import spacy

from spacy.matcher import PhraseMatcher

from .skills_db import SKILLS


nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(
    nlp.vocab,
    attr="LOWER",
)

patterns = [
    nlp.make_doc(skill)
    for skill in SKILLS
]

matcher.add(
    "SKILLS",
    patterns,
)


def extract_skills(job_description):
    """
    Extract skills from job description using NLP.
    """

    if not job_description:
        return []

    doc = nlp(job_description)

    matches = matcher(doc)

    found = set()

    for _, start, end in matches:

        skill = doc[start:end].text

        found.add(skill)

    return sorted(found)