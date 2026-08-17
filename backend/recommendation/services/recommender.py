# ============================================================
# RESUME AI - RECOMMENDATION SERVICE
# ============================================================


def generate_recommendations(resume, ats_analysis):

    # ========================================================
    # GET RESUME SKILLS
    # ========================================================

    skills = getattr(
        resume,
        "skills",
        []
    )

    print("========================================")
    print("RESUME SKILLS FROM DATABASE:")
    print(skills)
    print("========================================")


    # ========================================================
    # NORMALIZE SKILLS
    # ========================================================

    if isinstance(skills, dict):

        # Handle formats such as:
        # {"Python": "Programming", "Django": "Backend"}

        normalized_skills = []

        for key, value in skills.items():

            normalized_skills.append(
                str(key)
            )

            if isinstance(value, list):

                normalized_skills.extend(
                    str(item)
                    for item in value
                )

            elif value:

                normalized_skills.append(
                    str(value)
                )

        skills = normalized_skills


    elif isinstance(skills, str):

        # Handle comma-separated skills

        skills = [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]


    elif isinstance(skills, list):

        # Already a list

        skills = [
            str(skill).strip()
            for skill in skills
            if str(skill).strip()
        ]


    else:

        skills = []


    # ========================================================
    # CREATE SEARCH TEXT
    # ========================================================

    skill_text = " ".join(
        skills
    ).lower()


    print("NORMALIZED SKILLS:")
    print(skills)

    print("SKILL TEXT:")
    print(skill_text)


    # ========================================================
    # HELPER FUNCTION
    # ========================================================

    def has_skill(*keywords):

        return any(
            keyword.lower() in skill_text
            for keyword in keywords
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

        ats_score = float(
            ats_score
        )

    except (
        TypeError,
        ValueError
    ):

        ats_score = 0


    # ========================================================
    # RECOMMENDED ROLES
    # ========================================================

    recommended_roles = []


    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    if has_skill("python"):

        recommended_roles.extend([
            "Python Developer",
            "Python Full Stack Developer"
        ])


    # --------------------------------------------------------
    # DJANGO
    # --------------------------------------------------------

    if has_skill("django"):

        recommended_roles.extend([
            "Django Developer",
            "Python Backend Developer"
        ])


    # --------------------------------------------------------
    # FLASK
    # --------------------------------------------------------

    if has_skill("flask"):

        recommended_roles.extend([
            "Flask Developer",
            "Python Backend Developer"
        ])


    # --------------------------------------------------------
    # REACT / FRONTEND
    # --------------------------------------------------------

    if has_skill(
        "react",
        "react.js",
        "javascript",
        "html",
        "css"
    ):

        recommended_roles.extend([
            "Frontend Developer",
            "Web Developer"
        ])


    # --------------------------------------------------------
    # NODE.JS
    # --------------------------------------------------------

    if has_skill(
        "node",
        "node.js",
        "nodejs"
    ):

        recommended_roles.extend([
            "Node.js Developer",
            "Backend Developer"
        ])


    # --------------------------------------------------------
    # MACHINE LEARNING / AI
    # --------------------------------------------------------

    if has_skill(
        "machine learning",
        "machinelearning",
        "machine-learning",
        "artificial intelligence",
        "artificialintelligence",
        "ai",
        "ml"
    ):

        recommended_roles.extend([
            "Machine Learning Engineer",
            "AI Engineer"
        ])


    # --------------------------------------------------------
    # DATA SCIENCE
    # --------------------------------------------------------

    if has_skill(
        "data science",
        "datascience",
        "pandas",
        "numpy",
        "data analytics"
    ):

        recommended_roles.extend([
            "Data Scientist",
            "Data Analyst"
        ])


    # --------------------------------------------------------
    # SQL / DATABASE
    # --------------------------------------------------------

    if has_skill(
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "database"
    ):

        recommended_roles.extend([
            "Software Engineer",
            "Backend Developer"
        ])


    # --------------------------------------------------------
    # JAVA
    # --------------------------------------------------------

    if has_skill(
        "java",
        "spring",
        "spring boot"
    ):

        recommended_roles.extend([
            "Java Developer",
            "Backend Developer"
        ])


    # --------------------------------------------------------
    # C / C++
    # --------------------------------------------------------

    if has_skill(
        "c++",
        "cpp",
        "c programming"
    ):

        recommended_roles.append(
            "C++ Developer"
        )


    if has_skill("c"):

        recommended_roles.append(
            "Software Developer"
        )


    # --------------------------------------------------------
    # FULL STACK
    # --------------------------------------------------------

    has_backend = has_skill(
        "python",
        "django",
        "flask",
        "node",
        "node.js",
        "nodejs",
        "java",
        "spring",
        "spring boot"
    )


    has_frontend = has_skill(
        "react",
        "react.js",
        "javascript",
        "html",
        "css"
    )


    if (
        has_backend
        and has_frontend
    ):

        recommended_roles.append(
            "Full Stack Developer"
        )


    # --------------------------------------------------------
    # AI + PYTHON
    # --------------------------------------------------------

    if (
        has_skill("python")
        and has_skill(
            "machine learning",
            "machinelearning",
            "ml",
            "artificial intelligence",
            "ai"
        )
    ):

        recommended_roles.extend([
            "AI/ML Engineer",
            "Python AI Developer"
        ])


    # --------------------------------------------------------
    # REMOVE DUPLICATE ROLES
    # --------------------------------------------------------

    recommended_roles = list(
        dict.fromkeys(
            recommended_roles
        )
    )


    # ========================================================
    # DEFAULT ROLES
    # ========================================================

    if not recommended_roles:

        recommended_roles = [

            "Junior Software Developer",

            "Python Developer",

            "Software Engineer",

            "Web Developer"

        ]


    # ========================================================
    # LIMIT ROLES
    # ========================================================

    recommended_roles = (
        recommended_roles[:8]
    )


    # ========================================================
    # RECOMMENDED SKILLS
    # ========================================================

    recommended_skills = []


    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    if has_skill("python"):

        recommended_skills.extend([
            "Advanced Python",
            "Data Structures and Algorithms"
        ])

    else:

        recommended_skills.append(
            "Python"
        )


    # --------------------------------------------------------
    # DJANGO
    # --------------------------------------------------------

    if has_skill("django"):

        recommended_skills.append(
            "Django REST Framework"
        )

    else:

        recommended_skills.append(
            "Django"
        )


    # --------------------------------------------------------
    # REACT
    # --------------------------------------------------------

    if has_skill(
        "react",
        "react.js"
    ):

        recommended_skills.append(
            "React Hooks"
        )

    else:

        recommended_skills.append(
            "React.js"
        )


    # --------------------------------------------------------
    # JAVASCRIPT
    # --------------------------------------------------------

    if has_skill("javascript"):

        recommended_skills.append(
            "Advanced JavaScript"
        )

    else:

        recommended_skills.append(
            "JavaScript"
        )


    # --------------------------------------------------------
    # SQL
    # --------------------------------------------------------

    if has_skill(
        "sql",
        "mysql",
        "postgresql"
    ):

        recommended_skills.append(
            "Advanced SQL"
        )

    else:

        recommended_skills.append(
            "SQL"
        )


    # --------------------------------------------------------
    # MACHINE LEARNING
    # --------------------------------------------------------

    if has_skill(
        "machine learning",
        "machinelearning",
        "ml"
    ):

        recommended_skills.extend([
            "Deep Learning",
            "Model Deployment"
        ])

    else:

        recommended_skills.append(
            "Machine Learning"
        )


    # --------------------------------------------------------
    # ALWAYS USEFUL
    # --------------------------------------------------------

    recommended_skills.extend([
        "Git and GitHub",
        "REST API Development"
    ])


    # --------------------------------------------------------
    # REMOVE DUPLICATES
    # --------------------------------------------------------

    recommended_skills = list(
        dict.fromkeys(
            recommended_skills
        )
    )


    # ========================================================
    # COURSE RECOMMENDATIONS
    # ========================================================

    recommended_courses = []


    # Python

    recommended_courses.append({
        "title": "Python for Everybody",
        "platform": "Coursera",
        "level": "Beginner"
    })


    # Django

    recommended_courses.append({
        "title": "Django REST Framework",
        "platform": "Udemy",
        "level": "Intermediate"
    })


    # SQL

    recommended_courses.append({
        "title": "Advanced SQL",
        "platform": "Coursera",
        "level": "Intermediate"
    })


    # Machine Learning

    if has_skill(
        "machine learning",
        "machinelearning",
        "ml"
    ):

        recommended_courses.append({
            "title": "Machine Learning Specialization",
            "platform": "Coursera",
            "level": "Intermediate"
        })

    else:

        recommended_courses.append({
            "title": "Introduction to Machine Learning",
            "platform": "Coursera",
            "level": "Beginner"
        })


    # React

    if has_skill(
        "react",
        "react.js"
    ):

        recommended_courses.append({
            "title": "Advanced React Development",
            "platform": "Udemy",
            "level": "Intermediate"
        })

    else:

        recommended_courses.append({
            "title": "React.js for Beginners",
            "platform": "Udemy",
            "level": "Beginner"
        })


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
                "REST API"
            ]
        },


        {
            "title": "Job Recommendation System",

            "difficulty": "Intermediate",

            "technologies": [
                "Python",
                "Django",
                "Machine Learning",
                "SQL"
            ]
        },


        {
            "title": "AI Career Assistant",

            "difficulty": "Advanced",

            "technologies": [
                "Python",
                "Django",
                "React",
                "Machine Learning"
            ]
        },


        {
            "title": "Full Stack Job Portal",

            "difficulty": "Advanced",

            "technologies": [
                "Python",
                "Django",
                "React",
                "SQL"
            ]
        }

    ]


    # ========================================================
    # LEARNING ROADMAP
    # ========================================================

    learning_roadmap = {

        "Phase 1 - Programming":

            [
                "Strengthen Python fundamentals",
                "Practice Data Structures and Algorithms",
                "Improve problem-solving skills"
            ],


        "Phase 2 - Backend":

            [
                "Learn Django REST Framework",
                "Build REST APIs",
                "Practice JWT authentication"
            ],


        "Phase 3 - Database":

            [
                "Improve SQL skills",
                "Practice advanced SQL queries",
                "Learn database optimization"
            ],


        "Phase 4 - Frontend":

            [
                "Improve JavaScript",
                "Learn React.js",
                "Build responsive interfaces"
            ],


        "Phase 5 - AI and ML":

            [
                "Learn Machine Learning algorithms",
                "Practice model evaluation",
                "Learn model deployment"
            ],


        "Phase 6 - Portfolio":

            [
                "Build real-world projects",
                "Deploy projects",
                "Improve GitHub portfolio",
                "Prepare projects for interviews"
            ]

    }


    # ========================================================
    # RESUME TIPS
    # ========================================================

    if ats_score < 60:

        resume_tips = [

            "Improve keyword matching with job descriptions.",

            "Add measurable achievements to your experience.",

            "Include relevant technical skills.",

            "Improve your project descriptions.",

            "Keep your resume concise and ATS-friendly.",

            "Use clear section headings.",

            "Avoid unnecessary graphics and tables."

        ]


    elif ats_score < 80:

        resume_tips = [

            "Add more measurable achievements.",

            "Improve keyword relevance for target jobs.",

            "Strengthen your project descriptions.",

            "Add relevant technical keywords.",

            "Keep formatting simple and ATS-friendly.",

            "Customize your resume for each target role.",

            "Highlight your strongest technical skills."

        ]


    else:

        resume_tips = [

            "Maintain strong keyword alignment.",

            "Add measurable results to projects.",

            "Keep your technical skills updated.",

            "Continue improving your GitHub portfolio.",

            "Customize your resume for each target role.",

            "Use action verbs in your experience section.",

            "Keep the resume concise and professional."

        ]


    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    return {

        "resume_id":
            resume.id,


        "created":
            True,


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
            resume_tips

    }

