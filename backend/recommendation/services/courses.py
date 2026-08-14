"""
recommendation/services/courses.py

Course recommendation service.

Provides course recommendations based on
recommended career roles.
"""


# ============================================================
# Course Database
# ============================================================

COURSE_DATABASE = {

    "Backend Developer": [
        {
            "title": "Python Backend Development",
            "platform": "Coursera",
            "level": "Beginner",
            "skills": ["Python", "Backend Development"],
        },
        {
            "title": "Django Web Framework",
            "platform": "Udemy",
            "level": "Intermediate",
            "skills": ["Django", "Python"],
        },
        {
            "title": "Django REST Framework",
            "platform": "Udemy",
            "level": "Intermediate",
            "skills": ["Django", "REST API"],
        },
        {
            "title": "Docker for Developers",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["Docker", "DevOps"],
        },
    ],

    "Full Stack Developer": [
        {
            "title": "Full Stack Web Development",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["HTML", "CSS", "JavaScript", "React"],
        },
        {
            "title": "React.js Complete Guide",
            "platform": "Udemy",
            "level": "Intermediate",
            "skills": ["React", "JavaScript"],
        },
        {
            "title": "Django REST API Development",
            "platform": "Udemy",
            "level": "Intermediate",
            "skills": ["Django", "REST API"],
        },
        {
            "title": "Full Stack Development with React and Django",
            "platform": "YouTube",
            "level": "Advanced",
            "skills": ["React", "Django", "REST API"],
        },
    ],

    "Python Developer": [
        {
            "title": "Python Programming",
            "platform": "Coursera",
            "level": "Beginner",
            "skills": ["Python"],
        },
        {
            "title": "Object Oriented Programming with Python",
            "platform": "Udemy",
            "level": "Intermediate",
            "skills": ["Python", "OOP"],
        },
        {
            "title": "Python Data Structures and Algorithms",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["Python", "DSA"],
        },
        {
            "title": "Python Projects for Beginners",
            "platform": "YouTube",
            "level": "Beginner",
            "skills": ["Python"],
        },
    ],

    "Software Engineer": [
        {
            "title": "Data Structures and Algorithms",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["DSA", "Algorithms"],
        },
        {
            "title": "Software Engineering Principles",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["Software Engineering"],
        },
        {
            "title": "Git and GitHub",
            "platform": "Udemy",
            "level": "Beginner",
            "skills": ["Git", "GitHub"],
        },
        {
            "title": "Docker and DevOps Fundamentals",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["Docker", "DevOps"],
        },
    ],

    "Frontend Developer": [
        {
            "title": "HTML and CSS Fundamentals",
            "platform": "Coursera",
            "level": "Beginner",
            "skills": ["HTML", "CSS"],
        },
        {
            "title": "JavaScript Complete Course",
            "platform": "Udemy",
            "level": "Beginner",
            "skills": ["JavaScript"],
        },
        {
            "title": "React.js Development",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["React", "JavaScript"],
        },
        {
            "title": "Modern Frontend Development",
            "platform": "YouTube",
            "level": "Intermediate",
            "skills": ["React", "JavaScript", "CSS"],
        },
    ],

    "Python Django Developer": [
        {
            "title": "Python Django Development",
            "platform": "Udemy",
            "level": "Intermediate",
            "skills": ["Python", "Django"],
        },
        {
            "title": "Django REST Framework",
            "platform": "Udemy",
            "level": "Intermediate",
            "skills": ["Django", "REST API"],
        },
        {
            "title": "Building APIs with Django",
            "platform": "Coursera",
            "level": "Intermediate",
            "skills": ["Django", "REST API"],
        },
        {
            "title": "Django Deployment with Docker",
            "platform": "YouTube",
            "level": "Advanced",
            "skills": ["Django", "Docker"],
        },
    ],

}


# ============================================================
# Normalize Career Input
# ============================================================

def _normalize_careers(careers):
    """
    Convert career input into a clean list.
    """

    if not careers:
        return []

    if isinstance(careers, str):
        return [careers.strip()] if careers.strip() else []

    if isinstance(careers, (list, tuple, set)):
        return [
            str(career).strip()
            for career in careers
            if str(career).strip()
        ]

    return []


# ============================================================
# Recommend Courses
# ============================================================

def recommend_courses(careers):
    """
    Recommend courses based on career roles.

    Parameters
    ----------
    careers : list
        Recommended career roles.

    Returns
    -------
    list
        Recommended course dictionaries.
    """

    careers = _normalize_careers(careers)

    recommendations = []

    seen_courses = set()

    for career in careers:

        courses = COURSE_DATABASE.get(
            career,
            []
        )

        for course in courses:

            title = course.get("title", "")

            if not title:
                continue

            # Avoid duplicate courses
            if title in seen_courses:
                continue

            seen_courses.add(title)

            recommendations.append(
                {
                    "title": title,
                    "platform": course.get(
                        "platform",
                        "Online"
                    ),
                    "level": course.get(
                        "level",
                        "Beginner"
                    ),
                    "skills": course.get(
                        "skills",
                        []
                    ),
                    "career": career,
                }
            )

    return recommendations