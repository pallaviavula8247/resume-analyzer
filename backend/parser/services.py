import re

from .skills import extract_skills
from .education import extract_education
from .experience import extract_experience
from .projects import extract_projects


# ==========================================
# Extract Email
# ==========================================

def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else ""


# ==========================================
# Extract Phone Number
# ==========================================

def extract_phone(text):
    pattern = r"(\+91[\s-]?)?[6-9]\d{9}"
    match = re.search(pattern, text)
    return match.group(0) if match else ""


# ==========================================
# Extract Name
# ==========================================

def extract_name(text):

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    for line in lines[:5]:

        if (
            len(line.split()) <= 4
            and "@" not in line
            and not any(char.isdigit() for char in line)
        ):
            return line

    return ""


# ==========================================
# Extract LinkedIn
# ==========================================

def extract_linkedin(text):

    pattern = r"https?://(?:www\.)?linkedin\.com/[^\s]+"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


# ==========================================
# Extract GitHub
# ==========================================

def extract_github(text):

    pattern = r"https?://(?:www\.)?github\.com/[^\s]+"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


# ==========================================
# Extract Portfolio
# ==========================================

def extract_portfolio(text):

    urls = re.findall(r"https?://[^\s]+", text)

    for url in urls:

        lower = url.lower()

        if (
            "github" not in lower
            and "linkedin" not in lower
        ):
            return url

    return ""


# ==========================================
# Extract Location
# ==========================================

def extract_location(text):

    cities = [
        "Hyderabad",
        "Bangalore",
        "Chennai",
        "Mumbai",
        "Delhi",
        "Pune",
        "Kolkata",
        "Visakhapatnam",
        "Vijayawada",
        "Tirupati",
        "Rajampet",
        "Nellore",
        "Kurnool",
    ]

    for city in cities:
        if city.lower() in text.lower():
            return city

    return ""


# ==========================================
# Extract Certifications
# ==========================================

def extract_certifications(text):

    certifications = []

    keywords = [
        "AWS",
        "Azure",
        "Google Cloud",
        "Oracle",
        "Cisco",
        "Microsoft",
        "NPTEL",
        "Coursera",
        "Udemy",
        "Infosys Springboard",
        "AICTE",
    ]

    for keyword in keywords:
        if keyword.lower() in text.lower():
            certifications.append(keyword)

    return list(set(certifications))


# ==========================================
# Main Resume Parser
# ==========================================

def parse_resume(text):
    """
    Complete Resume Parsing Pipeline
    """

    data = {}

    # Personal Information
    data["full_name"] = extract_name(text)
    data["email"] = extract_email(text)
    data["phone"] = extract_phone(text)
    data["location"] = extract_location(text)
    data["linkedin"] = extract_linkedin(text)
    data["github"] = extract_github(text)
    data["portfolio"] = extract_portfolio(text)

    # Resume Sections
    data["skills"] = extract_skills(text)
    data["education"] = extract_education(text)
    data["experience"] = extract_experience(text)
    data["projects"] = extract_projects(text)
    data["certifications"] = extract_certifications(text)

    # Placeholder (implemented later)
    data["languages"] = []
    data["ats_score"] = 0
    data["missing_skills"] = []
    data["recommendations"] = []

    # Raw Resume Text
    data["raw_text"] = text

    return data