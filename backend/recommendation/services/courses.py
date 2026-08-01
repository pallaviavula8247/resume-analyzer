"""
courses.py

AI Course Recommendation Service

This module recommends courses based on
the candidate's missing skills.
"""


# ----------------------------------------
# Course Database
# ----------------------------------------

COURSE_DATABASE = {

    "Python": {
        "title": "Python for Everybody",
        "platform": "Coursera",
        "level": "Beginner",
    },

    "Django": {
        "title": "Django REST Framework Masterclass",
        "platform": "Udemy",
        "level": "Intermediate",
    },

    "Flask": {
        "title": "Flask Web Development",
        "platform": "Udemy",
        "level": "Intermediate",
    },

    "SQL": {
        "title": "SQL for Data Science",
        "platform": "Coursera",
        "level": "Beginner",
    },

    "MySQL": {
        "title": "MySQL Bootcamp",
        "platform": "Udemy",
        "level": "Beginner",
    },

    "MongoDB": {
        "title": "MongoDB Complete Developer Guide",
        "platform": "Udemy",
        "level": "Intermediate",
    },

    "React": {
        "title": "React Complete Guide",
        "platform": "Udemy",
        "level": "Intermediate",
    },

    "Angular": {
        "title": "Angular Crash Course",
        "platform": "Coursera",
        "level": "Intermediate",
    },

    "Docker": {
        "title": "Docker Essentials",
        "platform": "Udemy",
        "level": "Intermediate",
    },

    "Kubernetes": {
        "title": "Kubernetes for Beginners",
        "platform": "Udemy",
        "level": "Advanced",
    },

    "AWS": {
        "title": "AWS Cloud Practitioner",
        "platform": "Coursera",
        "level": "Beginner",
    },

    "Git": {
        "title": "Git & GitHub Complete Guide",
        "platform": "Coursera",
        "level": "Beginner",
    },

    "GitHub": {
        "title": "GitHub Essentials",
        "platform": "Coursera",
        "level": "Beginner",
    },

    "REST API": {
        "title": "REST API Development with Django",
        "platform": "Udemy",
        "level": "Intermediate",
    },

    "Machine Learning": {
        "title": "Machine Learning Specialization",
        "platform": "Coursera",
        "level": "Intermediate",
    },

    "Deep Learning": {
        "title": "Deep Learning Specialization",
        "platform": "Coursera",
        "level": "Advanced",
    },

    "TensorFlow": {
        "title": "TensorFlow Developer Certificate",
        "platform": "Coursera",
        "level": "Advanced",
    },

    "PyTorch": {
        "title": "PyTorch for Deep Learning",
        "platform": "Udemy",
        "level": "Advanced",
    },

    "NumPy": {
        "title": "NumPy for Data Science",
        "platform": "Coursera",
        "level": "Beginner",
    },

    "Pandas": {
        "title": "Data Analysis with Pandas",
        "platform": "Coursera",
        "level": "Beginner",
    },

    "Matplotlib": {
        "title": "Python Data Visualization",
        "platform": "Coursera",
        "level": "Beginner",
    },
}


# ----------------------------------------
# Recommendation Function
# ----------------------------------------

def recommend_courses(missing_skills):
    """
    Recommend courses based on missing skills.
    """

    recommendations = []

    for skill in missing_skills:

        if skill in COURSE_DATABASE:

            course = COURSE_DATABASE[skill].copy()
            course["skill"] = skill

            recommendations.append(course)

    return recommendations


# ----------------------------------------
# Testing
# ----------------------------------------

if __name__ == "__main__":

    skills = [
        "SQL",
        "Docker",
        "Git",
        "REST API",
    ]

    print(recommend_courses(skills))