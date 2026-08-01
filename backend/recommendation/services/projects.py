"""
projects.py

AI Project Recommendation Service

This module recommends projects based on
career goals and technical skills.
"""


# ----------------------------------------
# Project Database
# ----------------------------------------

PROJECT_DATABASE = {

    "Python Developer": [
        {
            "title": "Library Management System",
            "difficulty": "Beginner",
            "technologies": [
                "Python",
                "SQLite",
            ],
        },
        {
            "title": "Student Management System",
            "difficulty": "Intermediate",
            "technologies": [
                "Python",
                "Django",
                "SQLite",
            ],
        },
    ],

    "Backend Developer": [
        {
            "title": "REST API using Django REST Framework",
            "difficulty": "Intermediate",
            "technologies": [
                "Python",
                "Django",
                "REST API",
            ],
        },
        {
            "title": "Authentication API with JWT",
            "difficulty": "Advanced",
            "technologies": [
                "Django",
                "JWT",
                "PostgreSQL",
            ],
        },
    ],

    "Full Stack Developer": [
        {
            "title": "Resume Analyzer",
            "difficulty": "Advanced",
            "technologies": [
                "React",
                "Django",
                "REST API",
            ],
        },
        {
            "title": "E-Commerce Website",
            "difficulty": "Advanced",
            "technologies": [
                "React",
                "Django",
                "PostgreSQL",
            ],
        },
    ],

    "Data Analyst": [
        {
            "title": "Sales Dashboard",
            "difficulty": "Intermediate",
            "technologies": [
                "Python",
                "Pandas",
                "Matplotlib",
            ],
        },
        {
            "title": "Netflix Data Analysis",
            "difficulty": "Intermediate",
            "technologies": [
                "Python",
                "NumPy",
                "Pandas",
            ],
        },
    ],

    "Data Scientist": [
        {
            "title": "House Price Prediction",
            "difficulty": "Intermediate",
            "technologies": [
                "Python",
                "Scikit-learn",
                "Pandas",
            ],
        },
        {
            "title": "Customer Churn Prediction",
            "difficulty": "Advanced",
            "technologies": [
                "Machine Learning",
                "Python",
                "Pandas",
            ],
        },
    ],

    "AI Engineer": [
        {
            "title": "Resume Analyzer using NLP",
            "difficulty": "Advanced",
            "technologies": [
                "Python",
                "NLP",
                "Machine Learning",
            ],
        },
        {
            "title": "Medical Prescription OCR",
            "difficulty": "Advanced",
            "technologies": [
                "OCR",
                "OpenCV",
                "Python",
            ],
        },
    ],

    "Machine Learning Engineer": [
        {
            "title": "Disease Prediction System",
            "difficulty": "Advanced",
            "technologies": [
                "Machine Learning",
                "Python",
                "Scikit-learn",
            ],
        },
        {
            "title": "Recommendation System",
            "difficulty": "Advanced",
            "technologies": [
                "Python",
                "Pandas",
                "Machine Learning",
            ],
        },
    ],

    "Cloud Engineer": [
        {
            "title": "AWS EC2 Deployment",
            "difficulty": "Intermediate",
            "technologies": [
                "AWS",
                "Linux",
            ],
        },
        {
            "title": "Serverless Application",
            "difficulty": "Advanced",
            "technologies": [
                "AWS",
                "Lambda",
            ],
        },
    ],

    "DevOps Engineer": [
        {
            "title": "Dockerized Django App",
            "difficulty": "Intermediate",
            "technologies": [
                "Docker",
                "Django",
            ],
        },
        {
            "title": "CI/CD Pipeline",
            "difficulty": "Advanced",
            "technologies": [
                "GitHub Actions",
                "Docker",
            ],
        },
    ],
}


# ----------------------------------------
# Recommendation Function
# ----------------------------------------

def recommend_projects(careers):
    """
    Recommend projects based on career roles.

    Parameters
    ----------
    careers : list

    Returns
    -------
    list
    """

    recommendations = []

    for career in careers:

        if career in PROJECT_DATABASE:

            recommendations.extend(
                PROJECT_DATABASE[career]
            )

    return recommendations


# ----------------------------------------
# Testing
# ----------------------------------------

if __name__ == "__main__":

    careers = [
        "Python Developer",
        "Backend Developer",
    ]

    print(recommend_projects(careers))