/* =========================================================
   RESUME AI - AI RECOMMENDATIONS
   ========================================================= */

console.log("RECOMMENDATION.JS LOADED");


/* =========================================================
   AUTH CHECK
   ========================================================= */

if (
    typeof isAuthenticated === "function" &&
    !isAuthenticated()
) {
    window.location.href = "login.html";
}


/* =========================================================
   DOM ELEMENTS
   ========================================================= */

const loading =
    document.getElementById("recommendationLoading");

const section =
    document.getElementById("recommendationSection");

const grid =
    document.getElementById("recommendationGrid");

const emptyState =
    document.getElementById("recommendationEmpty");

const message =
    document.getElementById("recommendationMessage");

const resumeScore =
    document.getElementById("resumeScore");

const recommendationCount =
    document.getElementById("recommendationCount");

const resumeIdDisplay =
    document.getElementById("resumeIdDisplay");

const logoutButton =
    document.getElementById("logoutButton");

const menuButton =
    document.getElementById("menuButton");

const sidebar =
    document.getElementById("sidebar");


/* =========================================================
   SHOW MESSAGE
   ========================================================= */

function showMessage(text, type = "error") {

    if (!message) {
        console.error(text);
        return;
    }

    message.textContent = text;

    message.className =
        `recommendation-message ${type}`;

    message.style.display = "block";
}


/* =========================================================
   HIDE MESSAGE
   ========================================================= */

function hideMessage() {

    if (!message) {
        return;
    }

    message.textContent = "";

    message.style.display = "none";
}


/* =========================================================
   GET RESUME ID
   ========================================================= */

function getResumeId() {

    const resumeId =
        localStorage.getItem("resume_id");

    console.log(
        "RECOMMENDATION RESUME ID:",
        resumeId
    );

    return resumeId;
}


/* =========================================================
   LOAD RECOMMENDATIONS
   ========================================================= */

async function loadRecommendations() {

    console.log(
        "================================="
    );

    console.log(
        "LOADING AI RECOMMENDATIONS"
    );

    console.log(
        "================================="
    );


    const resumeId =
        getResumeId();


    /* =====================================================
       NO RESUME
       ===================================================== */

    if (!resumeId) {

        if (loading) {
            loading.style.display = "none";
        }

        if (section) {
            section.style.display = "none";
        }

        if (emptyState) {
            emptyState.style.display = "block";
        }

        showMessage(
            "No resume found. Please upload and analyze your resume first.",
            "error"
        );

        return;
    }


    /* =====================================================
       SHOW RESUME ID
       ===================================================== */

    if (resumeIdDisplay) {

        resumeIdDisplay.textContent =
            resumeId;

    }


    /* =====================================================
       LOADING
       ===================================================== */

    if (loading) {
        loading.style.display = "block";
    }

    if (section) {
        section.style.display = "none";
    }

    if (emptyState) {
        emptyState.style.display = "none";
    }

    hideMessage();


    try {

        /* =================================================
           API ENDPOINT
           ================================================= */

        const endpoint =
            `/recommendation/${resumeId}/`;


        console.log(
            "REQUESTING:",
            endpoint
        );


        /* =================================================
           API CALL
           ================================================= */

        const response =
            await apiGet(endpoint);


        console.log(
            "RECOMMENDATION API RESPONSE:",
            response
        );


        /* =================================================
           STOP LOADING
           ================================================= */

        if (loading) {
            loading.style.display = "none";
        }


        /* =================================================
           RENDER
           ================================================= */

        renderRecommendations(
            response
        );

    }

    catch (error) {

        console.error(
            "RECOMMENDATION ERROR:",
            error
        );


        if (loading) {
            loading.style.display = "none";
        }


        if (section) {
            section.style.display = "none";
        }


        if (emptyState) {
            emptyState.style.display = "none";
        }


        showMessage(
            error.message ||
            "Unable to load recommendations.",
            "error"
        );

    }

}


/* =========================================================
   EXTRACT API DATA
   ========================================================= */

function getRecommendationData(response) {

    if (
        response &&
        response.data
    ) {

        return response.data;

    }

    return response || {};

}


/* =========================================================
   EXTRACT ROLES
   ========================================================= */

function getRoles(data) {

    return Array.isArray(
        data.recommended_roles
    )
        ? data.recommended_roles
        : [];

}


/* =========================================================
   EXTRACT SKILLS
   ========================================================= */

function getSkills(data) {

    return Array.isArray(
        data.recommended_skills
    )
        ? data.recommended_skills
        : [];

}


/* =========================================================
   EXTRACT COURSES
   ========================================================= */

function getCourses(data) {

    return Array.isArray(
        data.recommended_courses
    )
        ? data.recommended_courses
        : [];

}


/* =========================================================
   EXTRACT PROJECTS
   ========================================================= */

function getProjects(data) {

    return Array.isArray(
        data.recommended_projects
    )
        ? data.recommended_projects
        : [];

}


/* =========================================================
   EXTRACT RESUME TIPS
   ========================================================= */

function getResumeTips(data) {

    return Array.isArray(
        data.resume_tips
    )
        ? data.resume_tips
        : [];

}


/* =========================================================
   EXTRACT ROADMAP
   ========================================================= */

function getRoadmap(data) {

    if (
        data.learning_roadmap &&
        typeof data.learning_roadmap === "object"
    ) {

        return data.learning_roadmap;

    }

    return {};

}


/* =========================================================
   EXTRACT SCORE
   ========================================================= */

function getScore(response, data) {

    const score =
        data.resume_score ??
        data.ats_score ??
        response.resume_score ??
        response.ats_score;

    if (
        score !== undefined &&
        score !== null
    ) {

        return score;

    }

    return "—";
}


/* =========================================================
   RENDER ALL RECOMMENDATIONS
   ========================================================= */

function renderRecommendations(response) {

    console.log(
        "RENDERING RECOMMENDATIONS..."
    );


    const data =
        getRecommendationData(
            response
        );


    const roles =
        getRoles(data);


    const skills =
        getSkills(data);


    const courses =
        getCourses(data);


    const projects =
        getProjects(data);


    const resumeTips =
        getResumeTips(data);


    const roadmap =
        getRoadmap(data);


    console.log(
        "ROLES:",
        roles
    );


    console.log(
        "SKILLS:",
        skills
    );


    console.log(
        "COURSES:",
        courses
    );


    console.log(
        "PROJECTS:",
        projects
    );


    console.log(
        "RESUME TIPS:",
        resumeTips
    );


    console.log(
        "ROADMAP:",
        roadmap
    );


    /* =====================================================
       SCORE
       ===================================================== */

    if (resumeScore) {

        resumeScore.textContent =
            getScore(
                response,
                data
            );

    }


    /* =====================================================
       COUNT
       ===================================================== */

    const totalRecommendations =
        roles.length +
        skills.length +
        courses.length +
        projects.length +
        resumeTips.length;


    if (recommendationCount) {

        recommendationCount.textContent =
            totalRecommendations;

    }


    /* =====================================================
       CLEAR OLD CONTENT
       ===================================================== */

    if (grid) {

        grid.innerHTML = "";

    }


    /* =====================================================
       CHECK EMPTY
       ===================================================== */

    if (
        roles.length === 0 &&
        skills.length === 0 &&
        courses.length === 0 &&
        projects.length === 0 &&
        resumeTips.length === 0
    ) {

        if (section) {
            section.style.display = "none";
        }

        if (emptyState) {
            emptyState.style.display = "block";
        }

        showMessage(
            "No recommendations are available for this resume.",
            "info"
        );

        return;
    }


    /* =====================================================
       HIDE EMPTY
       ===================================================== */

    if (emptyState) {

        emptyState.style.display =
            "none";

    }


    hideMessage();


    /* =====================================================
       BUILD CONTENT
       ===================================================== */

    let html = "";


    /* =====================================================
       ROLES
       ===================================================== */

    if (roles.length > 0) {

        html += createSection(
            "Recommended Roles",
            "Career roles that match your resume skills.",
            roles.map(
                (role, index) =>
                    createSimpleCard(
                        role,
                        index,
                        "ROLE"
                    )
            ).join("")
        );

    }


    /* =====================================================
       SKILLS
       ===================================================== */

    if (skills.length > 0) {

        html += createSection(
            "Recommended Skills",
            "Skills that can improve your career opportunities.",
            skills.map(
                (skill, index) =>
                    createSimpleCard(
                        skill,
                        index,
                        "SKILL"
                    )
            ).join("")
        );

    }


    /* =====================================================
       COURSES
       ===================================================== */

    if (courses.length > 0) {

        html += createSection(
            "Recommended Courses",
            "Courses selected to strengthen your technical profile.",
            courses.map(
                (course, index) =>
                    createCourseCard(
                        course,
                        index
                    )
            ).join("")
        );

    }


    /* =====================================================
       PROJECTS
       ===================================================== */

    if (projects.length > 0) {

        html += createSection(
            "Recommended Projects",
            "Projects you can build to strengthen your portfolio.",
            projects.map(
                (project, index) =>
                    createProjectCard(
                        project,
                        index
                    )
            ).join("")
        );

    }


    /* =====================================================
       RESUME TIPS
       ===================================================== */

    if (resumeTips.length > 0) {

        html += createSection(
            "Resume Improvement Tips",
            "Suggestions to improve your resume and ATS performance.",
            resumeTips.map(
                (tip, index) =>
                    createSimpleCard(
                        tip,
                        index,
                        "TIP"
                    )
            ).join("")
        );

    }


    /* =====================================================
       LEARNING ROADMAP
       ===================================================== */

    const roadmapKeys =
        Object.keys(roadmap);


    if (roadmapKeys.length > 0) {

        html += createRoadmapSection(
            roadmap
        );

    }


    /* =====================================================
       INSERT HTML
       ===================================================== */

    if (grid) {

        grid.innerHTML =
            html;

    }


    /* =====================================================
       SHOW SECTION
       ===================================================== */

    if (section) {

        section.style.display =
            "block";

    }

}


/* =========================================================
   CREATE SECTION
   ========================================================= */

function createSection(
    title,
    description,
    cards
) {

    return `

        <div class="recommendation-group">

            <div class="recommendation-group-header">

                <h2>
                    ${escapeHtml(title)}
                </h2>

                <p>
                    ${escapeHtml(description)}
                </p>

            </div>


            <div class="recommendation-cards">

                ${cards}

            </div>

        </div>

    `;

}


/* =========================================================
   SIMPLE CARD
   ========================================================= */

function createSimpleCard(
    value,
    index,
    label
) {

    return `

        <article class="recommendation-card">

            <div class="recommendation-number">

                ${String(index + 1).padStart(2, "0")}

            </div>


            <div class="recommendation-body">

                <div class="recommendation-card-label">

                    ${escapeHtml(label)}

                </div>


                <h3>

                    ${escapeHtml(value)}

                </h3>


                <div class="recommendation-card-footer">

                    <span>
                        ✦ ResumeAI
                    </span>

                    <span>
                        Personalized
                    </span>

                </div>

            </div>

        </article>

    `;

}


/* =========================================================
   COURSE CARD
   ========================================================= */

function createCourseCard(
    course,
    index
) {

    const title =
        course?.title ||
        "Recommended Course";


    const platform =
        course?.platform ||
        "Online";


    const level =
        course?.level ||
        "All Levels";


    return `

        <article class="recommendation-card">

            <div class="recommendation-number">

                ${String(index + 1).padStart(2, "0")}

            </div>


            <div class="recommendation-body">

                <div class="recommendation-card-label">

                    COURSE

                </div>


                <h3>

                    ${escapeHtml(title)}

                </h3>


                <p>

                    <strong>
                        Platform:
                    </strong>

                    ${escapeHtml(platform)}

                </p>


                <p>

                    <strong>
                        Level:
                    </strong>

                    ${escapeHtml(level)}

                </p>


                <div class="recommendation-card-footer">

                    <span>
                        ✦ ResumeAI
                    </span>

                    <span>
                        Learning
                    </span>

                </div>

            </div>

        </article>

    `;

}


/* =========================================================
   PROJECT CARD
   ========================================================= */

function createProjectCard(
    project,
    index
) {

    const title =
        project?.title ||
        "Recommended Project";


    const difficulty =
        project?.difficulty ||
        "Intermediate";


    const technologies =
        Array.isArray(
            project?.technologies
        )
            ? project.technologies
            : [];


    const technologyHtml =
        technologies
            .map(
                technology => `
                    <span class="technology-tag">
                        ${escapeHtml(technology)}
                    </span>
                `
            )
            .join("");


    return `

        <article class="recommendation-card">

            <div class="recommendation-number">

                ${String(index + 1).padStart(2, "0")}

            </div>


            <div class="recommendation-body">

                <div class="recommendation-card-label">

                    PROJECT

                </div>


                <h3>

                    ${escapeHtml(title)}

                </h3>


                <p>

                    <strong>
                        Difficulty:
                    </strong>

                    ${escapeHtml(difficulty)}

                </p>


                <div class="project-technologies">

                    ${technologyHtml}

                </div>


                <div class="recommendation-card-footer">

                    <span>
                        ✦ ResumeAI
                    </span>

                    <span>
                        Portfolio
                    </span>

                </div>

            </div>

        </article>

    `;

}


/* =========================================================
   ROADMAP SECTION
   ========================================================= */

function createRoadmapSection(
    roadmap
) {

    let roadmapHtml = "";


    Object.entries(
        roadmap
    ).forEach(
        (
            [phase, items]
        ) => {

            if (
                !Array.isArray(items)
            ) {
                return;
            }


            roadmapHtml += `

                <div class="roadmap-phase">

                    <h3>
                        ${escapeHtml(phase)}
                    </h3>


                    <ul>

                        ${items
                            .map(
                                item => `
                                    <li>
                                        ${escapeHtml(item)}
                                    </li>
                                `
                            )
                            .join("")
                        }

                    </ul>

                </div>

            `;

        }
    );


    if (!roadmapHtml) {
        return "";
    }


    return `

        <div class="recommendation-group roadmap-group">

            <div class="recommendation-group-header">

                <h2>
                    Learning Roadmap
                </h2>

                <p>
                    Follow these phases to strengthen your career profile.
                </p>

            </div>


            <div class="learning-roadmap">

                ${roadmapHtml}

            </div>

        </div>

    `;

}


/* =========================================================
   HTML SAFETY
   ========================================================= */

function escapeHtml(value) {

    return String(value)

        .replaceAll(
            "&",
            "&amp;"
        )

        .replaceAll(
            "<",
            "&lt;"
        )

        .replaceAll(
            ">",
            "&gt;"
        )

        .replaceAll(
            '"',
            "&quot;"
        )

        .replaceAll(
            "'",
            "&#039;"
        );

}


/* =========================================================
   LOGOUT
   ========================================================= */

if (logoutButton) {

    logoutButton.addEventListener(
        "click",
        function () {

            if (
                typeof logout ===
                "function"
            ) {

                logout();

            }

            else {

                localStorage.clear();

                window.location.href =
                    "login.html";

            }

        }
    );

}


/* =========================================================
   MOBILE MENU
   ========================================================= */

if (
    menuButton &&
    sidebar
) {

    menuButton.addEventListener(
        "click",
        function () {

            sidebar.classList.toggle(
                "open"
            );

        }
    );

}


/* =========================================================
   START
   ========================================================= */

loadRecommendations();

