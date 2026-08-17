/* =========================================================
   RESUME AI - JOB MATCH
   ========================================================= */

console.log("JOB-MATCH.JS LOADED");


/* =========================================================
   AUTH CHECK
   ========================================================= */

if (
    typeof isAuthenticated !== "function" ||
    !isAuthenticated()
) {
    window.location.href = "login.html";
}


/* =========================================================
   ELEMENTS
   ========================================================= */

const jobLoading =
    document.getElementById("jobLoading");

const jobError =
    document.getElementById("jobError");

const jobErrorMessage =
    document.getElementById("jobErrorMessage");

const jobResults =
    document.getElementById("jobResults");

const jobList =
    document.getElementById("jobList");

const totalJobs =
    document.getElementById("totalJobs");

const bestMatch =
    document.getElementById("bestMatch");

const resumeScore =
    document.getElementById("resumeScore");

const retryButton =
    document.getElementById("retryButton");

const logoutButton =
    document.getElementById("logoutButton");

const menuButton =
    document.getElementById("menuButton");

const sidebar =
    document.getElementById("sidebar");

const userAvatar =
    document.getElementById("userAvatar");

const topbarUserName =
    document.getElementById("topbarUserName");

const topbarUserEmail =
    document.getElementById("topbarUserEmail");


/* =========================================================
   DEBUG DOM
   ========================================================= */

console.log("JOB LOADING:", jobLoading);
console.log("JOB RESULTS:", jobResults);
console.log("JOB LIST:", jobList);


/* =========================================================
   LOAD USER
   ========================================================= */

async function loadUser() {

    try {

        const user =
            await apiGet("/users/profile/");

        console.log(
            "USER PROFILE:",
            user
        );

        const name =
            user?.full_name ||
            user?.username ||
            "User";


        if (topbarUserName) {

            topbarUserName.textContent =
                name;

        }


        if (topbarUserEmail) {

            topbarUserEmail.textContent =
                user?.email || "";

        }


        if (userAvatar) {

            userAvatar.textContent =
                name
                    .charAt(0)
                    .toUpperCase();

        }

    }

    catch (error) {

        console.error(
            "PROFILE LOAD ERROR:",
            error
        );

    }

}


/* =========================================================
   GET RESUME ID
   ========================================================= */

function getResumeId() {

    const resumeId =
        localStorage.getItem("resume_id");

    console.log(
        "STORED RESUME ID:",
        resumeId
    );

    return resumeId;

}


/* =========================================================
   SHOW ERROR
   ========================================================= */

function showJobError(message) {

    if (jobLoading) {

        jobLoading.style.display =
            "none";

    }


    if (jobResults) {

        jobResults.style.display =
            "none";

    }


    if (jobError) {

        jobError.style.display =
            "block";

    }


    if (jobErrorMessage) {

        jobErrorMessage.textContent =
            message;

    }

}


/* =========================================================
   LOAD JOB MATCHES
   ========================================================= */

async function loadJobMatches() {

    console.log(
        "===================================="
    );

    console.log(
        "LOADING JOB MATCHES"
    );

    console.log(
        "===================================="
    );


    const resumeId =
        getResumeId();


    if (!resumeId) {

        showJobError(
            "No resume ID found. Please upload and analyze your resume first."
        );

        return;

    }


    if (jobLoading) {

        jobLoading.style.display =
            "block";

    }


    if (jobError) {

        jobError.style.display =
            "none";

    }


    if (jobResults) {

        jobResults.style.display =
            "none";

    }


    try {

        const endpoint =
            `/analyzer/match/${resumeId}/`;


        console.log(
            "JOB MATCH API:",
            endpoint
        );


        const response =
            await apiGet(endpoint);


        console.log(
            "JOB MATCH RESPONSE:",
            response
        );


        if (jobLoading) {

            jobLoading.style.display =
                "none";

        }


        if (jobResults) {

            jobResults.style.display =
                "block";

        }


        renderJobMatches(
            response
        );

    }

    catch (error) {

        console.error(
            "JOB MATCH ERROR:",
            error
        );


        showJobError(
            error?.message ||
            "Unable to load job matches."
        );

    }

}


/* =========================================================
   EXTRACT DATA
   ========================================================= */

function extractJobData(response) {

    console.log(
        "EXTRACTING JOB DATA..."
    );


    /*
     * Possible response:
     *
     * {
     *   success: true,
     *   data: {
     *      jobs: [...]
     *   }
     * }
     */


    if (
        response &&
        typeof response === "object"
    ) {


        /* -----------------------------------------
           response.data
           ----------------------------------------- */

        if (
            response.data &&
            typeof response.data === "object"
        ) {

            return response.data;

        }


        /* -----------------------------------------
           response.jobs
           ----------------------------------------- */

        if (
            Array.isArray(
                response.jobs
            )
        ) {

            return response;

        }


        /* -----------------------------------------
           response.matches
           ----------------------------------------- */

        if (
            Array.isArray(
                response.matches
            )
        ) {

            return response;

        }


        /* -----------------------------------------
           response.job_matches
           ----------------------------------------- */

        if (
            Array.isArray(
                response.job_matches
            )
        ) {

            return response;

        }

    }


    return {};

}


/* =========================================================
   EXTRACT JOBS
   ========================================================= */

function extractJobs(response) {

    const data =
        extractJobData(response);


    console.log(
        "JOB DATA:",
        data
    );


    let jobs = [];


    /* -----------------------------------------
       jobs
       ----------------------------------------- */

    if (
        Array.isArray(data.jobs)
    ) {

        jobs =
            data.jobs;

    }


    /* -----------------------------------------
       matches
       ----------------------------------------- */

    else if (
        Array.isArray(data.matches)
    ) {

        jobs =
            data.matches;

    }


    /* -----------------------------------------
       job_matches
       ----------------------------------------- */

    else if (
        Array.isArray(data.job_matches)
    ) {

        jobs =
            data.job_matches;

    }


    /* -----------------------------------------
       recommended_jobs
       ----------------------------------------- */

    else if (
        Array.isArray(data.recommended_jobs)
    ) {

        jobs =
            data.recommended_jobs;

    }


    /* -----------------------------------------
       results
       ----------------------------------------- */

    else if (
        Array.isArray(data.results)
    ) {

        jobs =
            data.results;

    }


    console.log(
        "EXTRACTED JOBS:",
        jobs
    );


    return jobs;

}


/* =========================================================
   EXTRACT SCORE
   ========================================================= */

function extractScore(response) {

    const data =
        extractJobData(response);


    const score =
        data.resume_score ??
        data.ats_score ??
        data.match_score ??
        response?.resume_score ??
        response?.ats_score ??
        response?.match_score;


    if (
        score !== undefined &&
        score !== null
    ) {

        return score;

    }


    return null;

}


/* =========================================================
   RENDER JOB MATCHES
   ========================================================= */

function renderJobMatches(response) {

    console.log(
        "===================================="
    );

    console.log(
        "RENDERING JOB MATCHES"
    );

    console.log(
        "===================================="
    );


    const jobs =
        extractJobs(response);


    const score =
        extractScore(response);


    /* =====================================================
       TOTAL JOBS
       ===================================================== */

    if (totalJobs) {

        totalJobs.textContent =
            jobs.length;

    }


    /* =====================================================
       RESUME SCORE
       ===================================================== */

    if (resumeScore) {

        if (
            score !== null &&
            score !== ""
        ) {

            resumeScore.textContent =
                `${score}%`;

        }

        else {

            resumeScore.textContent =
                "—";

        }

    }


    /* =====================================================
       BEST MATCH
       ===================================================== */

    if (
        jobs.length > 0 &&
        bestMatch
    ) {

        const firstJob =
            jobs[0];


        bestMatch.textContent =
            firstJob.title ||
            firstJob.job_title ||
            firstJob.role ||
            firstJob.position ||
            "Job Role";

    }

    else if (bestMatch) {

        bestMatch.textContent =
            "—";

    }


    /* =====================================================
       CLEAR OLD JOBS
       ===================================================== */

    if (!jobList) {

        console.error(
            "jobList element not found."
        );

        return;

    }


    jobList.innerHTML =
        "";


    /* =====================================================
       NO JOBS
       ===================================================== */

    if (
        !jobs ||
        jobs.length === 0
    ) {

        jobList.innerHTML = `

            <div class="job-state">

                <div class="state-icon">
                    ⌕
                </div>

                <h3>
                    No job matches found
                </h3>

                <p>
                    The API returned no matching roles
                    for this resume.
                </p>

            </div>

        `;

        console.warn(
            "NO JOBS RETURNED BY API"
        );

        return;

    }


    /* =====================================================
       CREATE JOB CARDS
       ===================================================== */

    jobs.forEach(
        (job, index) => {

            createJobCard(
                job,
                index
            );

        }
    );

}


/* =========================================================
   CREATE JOB CARD
   ========================================================= */

function createJobCard(
    job,
    index
) {

    const title =
        job.title ||
        job.job_title ||
        job.role ||
        job.position ||
        `Job Role ${index + 1}`;


    const company =
        job.company ||
        job.company_name ||
        job.organization ||
        "ResumeAI Recommendation";


    const location =
        job.location ||
        job.city ||
        "Remote / Not specified";


    const jobType =
        job.job_type ||
        job.type ||
        job.employment_type ||
        "Full Time";


    const match =
        job.match_score ??
        job.score ??
        job.match_percentage ??
        job.match ??
        0;


    const description =
        job.description ||
        job.summary ||
        "This role matches your resume skills and qualifications.";


    const card =
        document.createElement("article");


    card.className =
        "job-card";


    card.innerHTML = `

        <div class="job-icon">

            ${escapeHtml(
                getJobInitial(title)
            )}

        </div>


        <div class="job-details">

            <div class="job-match-label">
                ${Number(match)}% Match
            </div>

            <h3>
                ${escapeHtml(title)}
            </h3>

            <div class="job-company">
                ${escapeHtml(company)}
            </div>

            <div class="job-meta">

                <span>
                    📍 ${escapeHtml(location)}
                </span>

                <span>
                    💼 ${escapeHtml(jobType)}
                </span>

            </div>

            <p class="job-description">
                ${escapeHtml(description)}
            </p>

        </div>


        <div class="job-match-score">

            <div class="match-score-circle">
                ${Number(match)}%
            </div>

            <small>
                Match
            </small>

        </div>

    `;


    if (jobList) {

        jobList.appendChild(
            card
        );

    }

}


/* =========================================================
   JOB INITIAL
   ========================================================= */

function getJobInitial(title) {

    if (!title) {

        return "J";

    }


    return title
        .trim()
        .charAt(0)
        .toUpperCase();

}


/* =========================================================
   HTML ESCAPE
   ========================================================= */

function escapeHtml(value) {

    return String(value ?? "")
        .replace(
            /&/g,
            "&amp;"
        )
        .replace(
            /</g,
            "&lt;"
        )
        .replace(
            />/g,
            "&gt;"
        )
        .replace(
            /"/g,
            "&quot;"
        )
        .replace(
            /'/g,
            "&#039;"
        );

}


/* =========================================================
   RETRY
   ========================================================= */

if (retryButton) {

    retryButton.addEventListener(
        "click",
        loadJobMatches
    );

}


/* =========================================================
   LOGOUT
   ========================================================= */

if (logoutButton) {

    logoutButton.addEventListener(
        "click",
        logout
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
        () => {

            sidebar.classList.toggle(
                "open"
            );

        }
    );

}


/* =========================================================
   INITIALIZE
   ========================================================= */

console.log(
    "INITIALIZING JOB MATCH PAGE"
);

console.log(
    "AUTHENTICATED:",
    typeof isAuthenticated === "function"
        ? isAuthenticated()
        : "AUTH FUNCTION NOT FOUND"
);

console.log(
    "RESUME ID:",
    localStorage.getItem("resume_id")
);


loadUser();

loadJobMatches();

