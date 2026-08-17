# ============================================================
# RESUME AI - RECOMMENDATION SERVICES
# ============================================================

def generate_recommendations(resume, ats_analysis):

    # ========================================================
    # GET RESUME SKILLS
    # ========================================================

    skills = getattr(resume, "skills", [])

    if not isinstance(skills, list):
        skills = []

    skills = [
        str(skill).strip()
        for skill in skills
        if str(skill).strip()
    ]

    skill_text = " ".join(
        skill.lower()
        for skill in skills
    )


    # ========================================================
    # GET ATS SCORE
    # ========================================================

    ats_score = getattr(
        ats_analysis,
        "ats_score",
        0
    )

    try:
        ats_score = float(ats_score)
    except (TypeError, ValueError):
        ats_score = 0


    # ========================================================
    # RECOMMENDED ROLES
    # ========================================================

    if "python" in skill_text:

        recommended_roles = [
            "Python Developer",
            "Python Backend Developer",
            "Junior Software Developer",
        ]

        if "django" in skill_text:

            recommended_roles.append(
                "Django Developer"
            )

        if "react" in skill_text:

            recommended_roles.append(
                "Python Full Stack Developer"
            )

    else:

        recommended_roles = [
            "Junior Software Developer",
            "Software Engineer",
            "Python Developer",
        ]


    # ========================================================
    # RECOMMENDED SKILLS
    # ========================================================

    recommended_skills = []


    if "python" in skill_text:

        recommended_skills.extend([
            "Advanced Python",
            "REST API Development",
            "Object-Oriented Programming",
        ])


    if "django" in skill_text:

        recommended_skills.extend([
            "Django REST Framework",
            "JWT Authentication",
        ])


    if "javascript" in skill_text:

        recommended_skills.extend([
            "Modern JavaScript",
            "Async/Await",
            "API Integration",
        ])


    if "react" in skill_text:

        recommended_skills.extend([
            "React Hooks",
            "State Management",
        ])


    if "sql" in skill_text:

        recommended_skills.extend([
            "Advanced SQL",
            "Database Design",
        ])


    if "machine learning" in skill_text:

        recommended_skills.extend([
            "Model Deployment",
            "Feature Engineering",
            "ML Model Evaluation",
        ])


    if not recommended_skills:

        recommended_skills = [
            "Python",
            "SQL",
            "Git and GitHub",
            "REST APIs",
            "Problem Solving",
        ]


    # Remove duplicates
    recommended_skills = list(
        dict.fromkeys(
            recommended_skills
        )
    )


    # ========================================================
    # COURSE RECOMMENDATIONS
    # ========================================================

    recommended_courses = [

        {
            "title": "Python for Everybody",
            "platform": "Coursera",
            "level": "Beginner",
        },

        {
            "title": "Django REST Framework",
            "platform": "Udemy",
            "level": "Intermediate",
        },

        {
            "title": "SQL for Data Science",
            "platform": "Coursera",
            "level": "Intermediate",
        },

    ]


    # ========================================================
    # PROJECT RECOMMENDATIONS
    # ========================================================

    recommended_projects = [

        {
            "title": "AI Resume Analyzer",
            "difficulty": "Intermediate",
            "technologies": [
                "Python",
                "Django",
                "NLP",
                "REST API",
            ],
        },

        {
            "title": "Job Recommendation System",
            "difficulty": "Intermediate",
            "technologies": [
                "Python",
                "Machine Learning",
                "Django",
                "SQL",
            ],
        },

    ]


    # ========================================================
    # LEARNING ROADMAP
    # ========================================================

    learning_roadmap = {

        "Phase 1": [
            "Strengthen Python fundamentals",
            "Practice Data Structures and Algorithms",
        ],

        "Phase 2": [
            "Learn Django REST Framework",
            "Build REST APIs",
        ],

        "Phase 3": [
            "Improve SQL and database skills",
            "Practice real-world SQL queries",
        ],

        "Phase 4": [
            "Build and deploy full-stack projects",
            "Improve GitHub portfolio",
        ],

    }


    # ========================================================
    # RESUME IMPROVEMENT TIPS
    # ========================================================

    if ats_score < 60:

        resume_tips = [

            "Improve keyword matching with job descriptions.",

            "Add measurable achievements to your experience.",

            "Include relevant technical skills.",

            "Improve project descriptions.",

        ]

    elif ats_score < 80:

        resume_tips = [

            "Add more measurable achievements.",

            "Improve keyword relevance for target roles.",

            "Strengthen your project descriptions.",

            "Keep your resume concise and achievement-focused.",

        ]

    else:

        resume_tips = [

            "Maintain strong keyword alignment.",

            "Add measurable results to projects.",

            "Keep technical skills updated.",

            "Continue improving your GitHub portfolio.",

        ]


    # ========================================================
    # FINAL DATA
    # ========================================================

    return {

        "resume_id": resume.id,

        "created": True,

        "recommended_roles":
            recommended_roles,

        "recommended_skills":
            recommended_skills,

        "recommended_courses":
            recommended_courses,

        "recommended_projects":
            recommended_projects,

        "learning_roadmap":
            learning_roadmap,

        "resume_tips":
            resume_tips,

    }