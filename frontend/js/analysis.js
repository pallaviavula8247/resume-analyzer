/* =========================================================
   RESUME AI - ANALYSIS
   ========================================================= */


/* =========================================================
   AUTHENTICATION
   ========================================================= */

if (!isAuthenticated()) {

    window.location.href =
        "login.html";

}


/* =========================================================
   ELEMENTS
   ========================================================= */

const analysisLoading =
    document.getElementById(
        "analysisLoading"
    );

const analysisError =
    document.getElementById(
        "analysisError"
    );

const analysisResults =
    document.getElementById(
        "analysisResults"
    );


const atsScore =
    document.getElementById(
        "atsScore"
    );

const keywordScore =
    document.getElementById(
        "keywordScore"
    );

const skillScore =
    document.getElementById(
        "skillScore"
    );

const experienceScore =
    document.getElementById(
        "experienceScore"
    );

const scoreStatus =
    document.getElementById(
        "scoreStatus"
    );


const strengthsList =
    document.getElementById(
        "strengthsList"
    );

const weaknessesList =
    document.getElementById(
        "weaknessesList"
    );

const missingSkills =
    document.getElementById(
        "missingSkills"
    );

const recommendationsList =
    document.getElementById(
        "recommendationsList"
    );


const logoutButton =
    document.getElementById(
        "logoutButton"
    );

const menuButton =
    document.getElementById(
        "menuButton"
    );

const sidebar =
    document.getElementById(
        "sidebar"
    );


const userAvatar =
    document.getElementById(
        "userAvatar"
    );

const topbarUserName =
    document.getElementById(
        "topbarUserName"
    );

const topbarUserEmail =
    document.getElementById(
        "topbarUserEmail"
    );


/* =========================================================
   RESUME ID
   ========================================================= */

const resumeId =
    localStorage.getItem(
        "resume_id"
    );


/* =========================================================
   LOAD USER
   ========================================================= */

async function loadUser() {

    try {

        const user =
            await apiGet(
                "/users/profile/"
            );


        const fullName =
            user.full_name || "User";


        topbarUserName.textContent =
            fullName;


        topbarUserEmail.textContent =
            user.email || "";


        userAvatar.textContent =
            fullName
                .charAt(0)
                .toUpperCase();

    }

    catch (error) {

        console.error(
            "PROFILE LOAD ERROR:",
            error
        );

    }

}


/* =========================================================
   SHOW ERROR
   ========================================================= */

function showAnalysisError(
    message
) {

    analysisLoading.style.display =
        "none";

    analysisResults.style.display =
        "none";

    analysisError.textContent =
        message;

    analysisError.style.display =
        "block";

}


/* =========================================================
   FORMAT SCORE
   ========================================================= */

function formatScore(
    value
) {

    const number =
        Number(value);

    if (
        Number.isNaN(number)
    ) {

        return 0;

    }

    return Math.round(
        number
    );

}


/* =========================================================
   SCORE STATUS
   ========================================================= */

function getScoreStatus(
    score
) {

    if (score >= 80) {

        return "Excellent";

    }

    if (score >= 60) {

        return "Good";

    }

    if (score >= 40) {

        return "Needs Improvement";

    }

    return "Needs Attention";

}


/* =========================================================
   RENDER ARRAY
   ========================================================= */

function renderList(
    element,
    items,
    emptyMessage
) {

    element.innerHTML = "";


    if (
        !Array.isArray(items) ||
        items.length === 0
    ) {

        const li =
            document.createElement(
                "li"
            );

        li.textContent =
            emptyMessage;

        element.appendChild(
            li
        );

        return;

    }


    items.forEach(
        item => {

            const li =
                document.createElement(
                    "li"
                );


            if (
                typeof item === "object"
            ) {

                li.textContent =
                    item.text ||
                    item.message ||
                    item.name ||
                    JSON.stringify(item);

            }

            else {

                li.textContent =
                    String(item);

            }


            element.appendChild(
                li
            );

        }
    );

}


/* =========================================================
   RENDER SKILLS
   ========================================================= */

function renderSkills(
    skills
) {

    missingSkills.innerHTML = "";


    if (
        !Array.isArray(skills) ||
        skills.length === 0
    ) {

        missingSkills.innerHTML =
            "<span>No major missing skills identified.</span>";

        return;

    }


    skills.forEach(
        skill => {

            const span =
                document.createElement(
                    "span"
                );


            if (
                typeof skill === "object"
            ) {

                span.textContent =
                    skill.name ||
                    skill.skill ||
                    JSON.stringify(skill);

            }

            else {

                span.textContent =
                    String(skill);

            }


            missingSkills.appendChild(
                span
            );

        }
    );

}


/* =========================================================
   RENDER RECOMMENDATIONS
   ========================================================= */

function renderRecommendations(
    recommendations
) {

    recommendationsList.innerHTML =
        "";


    if (
        !Array.isArray(recommendations) ||
        recommendations.length === 0
    ) {

        recommendationsList.innerHTML =
            "<p>No recommendations available.</p>";

        return;

    }


    recommendations.forEach(
        (recommendation, index) => {

            const item =
                document.createElement(
                    "div"
                );

            item.className =
                "recommendation-item";


            const number =
                document.createElement(
                    "span"
                );

            number.className =
                "recommendation-number";

            number.textContent =
                String(index + 1)
                    .padStart(
                        2,
                        "0"
                    );


            const text =
                document.createElement(
                    "p"
                );


            if (
                typeof recommendation ===
                "object"
            ) {

                text.textContent =
                    recommendation.text ||
                    recommendation.message ||
                    recommendation.description ||
                    JSON.stringify(
                        recommendation
                    );

            }

            else {

                text.textContent =
                    String(
                        recommendation
                    );

            }


            item.appendChild(
                number
            );

            item.appendChild(
                text
            );


            recommendationsList.appendChild(
                item
            );

        }
    );

}


/* =========================================================
   LOAD ANALYSIS
   ========================================================= */

async function loadAnalysis() {

    if (!resumeId) {

        showAnalysisError(
            "No resume was found. Please upload your resume first."
        );

        return;

    }


    console.log(
        "ANALYZING RESUME ID:",
        resumeId
    );


    try {

        const response =
            await apiGet(
                `/analyzer/analyze/${resumeId}/`
            );


        console.log(
            "ANALYSIS RESPONSE:",
            response
        );


        /*
         * Support both:
         *
         * {
         *     ats_score: 85
         * }
         *
         * and:
         *
         * {
         *     data: {
         *         ats_score: 85
         *     }
         * }
         */

        const data =
            response?.data ||
            response;


        const ats =
            formatScore(
                data.ats_score
            );


        const keyword =
            formatScore(
                data.keyword_score
            );


        const skill =
            formatScore(
                data.skill_score
            );


        const experience =
            formatScore(
                data.experience_score
            );


        /* =================================================
           SCORES
           ================================================= */

        atsScore.textContent =
            ats;


        keywordScore.textContent =
            keyword;


        skillScore.textContent =
            skill;


        experienceScore.textContent =
            experience;


        scoreStatus.textContent =
            getScoreStatus(
                ats
            );


        /* =================================================
           STRENGTHS
           ================================================= */

        renderList(
            strengthsList,
            data.strengths,
            "No strengths available."
        );


        /* =================================================
           WEAKNESSES
           ================================================= */

        renderList(
            weaknessesList,
            data.weaknesses,
            "No major weaknesses identified."
        );


        /* =================================================
           MISSING SKILLS
           ================================================= */

        renderSkills(
            data.missing_skills
        );


        /* =================================================
           RECOMMENDATIONS
           ================================================= */

        renderRecommendations(
            data.recommendations
        );


        /* =================================================
           SHOW RESULTS
           ================================================= */

        analysisLoading.style.display =
            "none";

        analysisError.style.display =
            "none";

        analysisResults.style.display =
            "block";


    }

    catch (error) {

        console.error(
            "ANALYSIS ERROR:",
            error
        );


        showAnalysisError(
            error.message ||
            "Unable to analyze your resume."
        );

    }

}


/* =========================================================
   LOGOUT
   ========================================================= */

logoutButton.addEventListener(
    "click",
    () => {

        logout();

    }
);


/* =========================================================
   MOBILE MENU
   ========================================================= */

menuButton.addEventListener(
    "click",
    () => {

        sidebar.classList.toggle(
            "open"
        );

    }
);


/* =========================================================
   INITIALIZE
   ========================================================= */

loadUser();

loadAnalysis();