"""
roadmap.py

Learning Roadmap Recommendation Service
"""


ROADMAP_DATABASE = {

    "Python Developer": [
        "Learn Python Basics",
        "Master Object-Oriented Programming",
        "Practice File Handling",
        "Learn Exception Handling",
        "Understand Modules and Packages",
        "Practice SQL",
        "Learn Git & GitHub",
        "Build Python Projects",
    ],

    "Backend Developer": [
        "Master Python",
        "Learn Django",
        "Learn Django REST Framework",
        "Build REST APIs",
        "Learn JWT Authentication",
        "Practice PostgreSQL",
        "Learn Docker",
        "Deploy Applications",
    ],

    "Full Stack Developer": [
        "Master HTML",
        "Master CSS",
        "Learn JavaScript",
        "Learn React",
        "Master Python",
        "Learn Django",
        "Build REST APIs",
        "Connect React with Django",
        "Deploy Full Stack Applications",
    ],

    "Data Analyst": [
        "Master Python",
        "Learn NumPy",
        "Learn Pandas",
        "Learn Matplotlib",
        "Practice SQL",
        "Learn Excel",
        "Create Dashboards",
        "Practice Data Cleaning",
    ],

    "Data Scientist": [
        "Master Python",
        "Learn Statistics",
        "Learn NumPy",
        "Learn Pandas",
        "Learn Machine Learning",
        "Study Scikit-learn",
        "Build ML Projects",
        "Deploy ML Models",
    ],

    "Machine Learning Engineer": [
        "Master Python",
        "Learn Mathematics",
        "Study Machine Learning",
        "Practice Feature Engineering",
        "Learn Deep Learning",
        "Study TensorFlow",
        "Study PyTorch",
        "Deploy ML Models",
    ],

    "AI Engineer": [
        "Master Python",
        "Learn Machine Learning",
        "Study Deep Learning",
        "Learn NLP",
        "Study Computer Vision",
        "Practice TensorFlow",
        "Practice PyTorch",
        "Build AI Projects",
    ],

    "Cloud Engineer": [
        "Learn Linux",
        "Study Networking",
        "Learn AWS",
        "Practice EC2",
        "Practice S3",
        "Learn IAM",
        "Deploy Cloud Applications",
    ],

    "DevOps Engineer": [
        "Learn Linux",
        "Master Git",
        "Learn Docker",
        "Study Kubernetes",
        "Learn Jenkins",
        "Practice CI/CD",
        "Deploy Cloud Applications",
    ],
}


def generate_roadmap(career):
    """
    Returns a learning roadmap
    for the selected career.
    """

    return ROADMAP_DATABASE.get(
        career,
        [
            "Choose a career path.",
            "Learn the required technologies.",
            "Build projects.",
            "Apply for internships.",
        ],
    )


if __name__ == "__main__":

    roadmap = generate_roadmap(
        "AI Engineer"
    )

    print(roadmap)