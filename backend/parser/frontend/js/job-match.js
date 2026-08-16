/* =========================================================
   RESUME AI - JOB MATCH
   ========================================================= */


/* =========================================================
   AUTH
   ========================================================= */

if (!isAuthenticated()) {

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
   LOAD USER
   ========================================================= */

async function loadUser() {

    try {

        const user =
            await apiGet(
                "/users/profile/"
            );

        const name =
            user.full_name || "User";

        topbarUserName.textContent =
            name;

        topbarUserEmail.textContent =
            user.email || "";

        userAvatar.textContent =
            name
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
   GET RESUME ID
   ========================================================= */

function getResumeId() {

    return localStorage.getItem(
        "resume_id"
    );

}


/* =========================================================
   SHOW ERROR
   ========================================================= */

function showJobError(message) {

    jobLoading.style.display =
        "none";

    jobResults.style.display =
        "none";

    jobError.style.display =
        "block";

    jobErrorMessage.textContent =
        message;

}


/* =========================================================
   LOAD JOB MATCHES
   ========================================================= */

async function loadJobMatches() {

    const resumeId =
        getResumeId();

    console.log(
        "RESUME ID:",
        resumeId
    );


    if (!resumeId) {

        showJobError(
            "No uploaded resume was found. Please upload your resume first."
        );

        return;

    }


    jobLoading.style.display =
        "block";

    jobError.style.display =
        "none";

    jobResults.style.display =
        "none";


    try {

        const response =
            await apiGet(
                `/analyzer/match/${resumeId}/`
            );


        console.log(
            "JOB MATCH RESPONSE:",
            response
        );


        jobLoading.style.display =
            "none";

        jobResults.style.display =
            "block";


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
            error.message ||
            "Unable to load job matches."
        );

    }

}


/* =========================================================
   RENDER RESULTS
   ========================================================= */

function renderJobMatches(response) {

    /*
     * Supports common backend response formats.
     */

    const data =
        response?.data || response || {};


    let jobs =
        data.jobs ||
        data.matches ||
        data.job_matches ||
        [];


    if (!Array.isArray(jobs)) {

        jobs = [];

    }


    totalJobs.textContent =
        jobs.length;


    const score =
        data.resume_score ??
        data.ats_score ??
        data.match_score;


    resumeScore.textContent =
        score !== undefined &&
        score !== null
            ? `${score}%`
            : "—";


    if (jobs.length > 0) {

        const firstJob =
            jobs[0];

        bestMatch.textContent =
            firstJob.title ||
            firstJob.job_title ||
            "—";

    }

    else {

        bestMatch.textContent =
            "—";

    }


    jobList.innerHTML = "";


    if (jobs.length === 0) {

        jobList.innerHTML = `

            <div class="job-state">

                <div class="state-icon">
                    ?
                </div>

                <h3>
                    No job matches found
                </h3>

                <p>
                    Try improving your resume skills
                    and experience information.
                </p>

            </div>

        `;

        return;

    }


    jobs.forEach(
        (job, index) => {

            const title =
                job.title ||
                job.job_title ||
                job.role ||
                "Job Role";


            const company =
                job.company ||
                job.company_name ||
                "Company";


            const location =
                job.location ||
                "Not specified";


            const jobType =
                job.job_type ||
                job.type ||
                "Full Time";


            const match =
                job.match_score ??
                job.score ??
                job.match_percentage ??
                0;


            const card =
                document.createElement(
                    "div"
                );


            card.className =
                "job-card";


            card.innerHTML = `

                <div class="job-icon">
                    ${getJobInitial(title)}
                </div>


                <div class="job-details">

                    <h3>
                        ${escapeHtml(title)}
                    </h3>

                    <div class="job-company">
                        ${escapeHtml(company)}
                    </div>

                    <div class="job-meta">

                        <span>
                            ${escapeHtml(location)}
                        </span>

                        <span>
                            ${escapeHtml(jobType)}
                        </span>

                    </div>

                </div>


                <div class="job-match-score">

                    <div class="match-score-circle">
                        ${match}%
                    </div>

                    <small>
                        Match
                    </small>

                </div>

            `;


            jobList.appendChild(
                card
            );

        }
    );

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

    return String(value)
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

retryButton.addEventListener(
    "click",
    loadJobMatches
);


/* =========================================================
   LOGOUT
   ========================================================= */

logoutButton.addEventListener(
    "click",
    logout
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

loadJobMatches();