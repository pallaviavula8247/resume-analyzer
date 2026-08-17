/* =========================================================
   RESUME AI - REPORTS
   ========================================================= */


/* =========================================================
   AUTHENTICATION
   ========================================================= */

if (!isAuthenticated()) {
    window.location.href = "login.html";
}


/* =========================================================
   ELEMENTS
   ========================================================= */

const reportLoading =
    document.getElementById("reportLoading");

const reportMessage =
    document.getElementById("reportMessage");

const reportSummary =
    document.getElementById("reportSummary");

const reportList =
    document.getElementById("reportList");

const totalReports =
    document.getElementById("totalReports");

const latestATS =
    document.getElementById("latestATS");

const latestMatch =
    document.getElementById("latestMatch");

const generateReportButton =
    document.getElementById("generateReportButton");

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
   GET CURRENT RESUME ID
   ========================================================= */

function getResumeId() {

    const resumeId =
        localStorage.getItem("resume_id");

    console.log(
        "CURRENT STORED RESUME ID:",
        resumeId
    );

    return resumeId;

}


/* =========================================================
   LOAD USER
   ========================================================= */

async function loadUser() {

    try {

        const response =
            await apiGet(
                "/users/profile/"
            );

        const user =
            response.user ||
            response.data ||
            response;

        const name =
            user.full_name ||
            user.name ||
            "User";

        if (topbarUserName) {

            topbarUserName.textContent =
                name;

        }

        if (topbarUserEmail) {

            topbarUserEmail.textContent =
                user.email || "";

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
            "PROFILE ERROR:",
            error
        );

    }

}


/* =========================================================
   SHOW MESSAGE
   ========================================================= */

function showMessage(
    message,
    type = "success"
) {

    if (!reportMessage) {
        return;
    }

    reportMessage.textContent =
        message;

    reportMessage.className =
        `report-message ${type}`;

    reportMessage.style.display =
        "block";

}


/* =========================================================
   HIDE MESSAGE
   ========================================================= */

function hideMessage() {

    if (!reportMessage) {
        return;
    }

    reportMessage.style.display =
        "none";

}


/* =========================================================
   LOAD REPORT HISTORY
   ========================================================= */

async function loadReports() {

    try {

        console.log(
            "================================"
        );

        console.log(
            "LOADING REPORT HISTORY"
        );

        console.log(
            "================================"
        );


        const response =
            await apiGet(
                "/reports/"
            );


        console.log(
            "REPORT API RESPONSE:",
            response
        );


        const reports =
            response.reports ||
            response.history ||
            response.data ||
            [];


        console.log(
            "REPORTS FOUND:",
            reports.length
        );


        renderReports(
            reports
        );

    }

    catch (error) {

        console.error(
            "REPORT LOAD ERROR:",
            error
        );


        if (reportList) {

            reportList.innerHTML = `

                <div class="report-state error-state">

                    <div class="state-icon">
                        !
                    </div>

                    <h3>
                        Unable to load reports
                    </h3>

                    <p>
                        ${escapeHtml(
                            error.message ||
                            "Something went wrong."
                        )}
                    </p>

                </div>

            `;

        }

    }

}


/* =========================================================
   RENDER REPORTS
   ========================================================= */

function renderReports(
    reports
) {

    if (!Array.isArray(reports)) {

        reports = [];

    }


    /*
     * Backend already returns reports
     * ordered by newest first.
     */

    reports.sort(
        (a, b) => {

            return new Date(
                b.generated_at || 0
            ) -
            new Date(
                a.generated_at || 0
            );

        }
    );


    if (totalReports) {

        totalReports.textContent =
            reports.length;

    }


    if (reportSummary) {

        reportSummary.style.display =
            "grid";

    }


    /* =====================================================
       NO REPORTS
    ===================================================== */

    if (reports.length === 0) {

        if (latestATS) {

            latestATS.textContent =
                "—";

        }

        if (latestMatch) {

            latestMatch.textContent =
                "—";

        }


        if (reportList) {

            reportList.innerHTML = `

                <div class="report-state">

                    <div class="state-icon">
                        ▤
                    </div>

                    <h3>
                        No reports yet
                    </h3>

                    <p>
                        Generate your first resume
                        analysis report.
                    </p>

                </div>

            `;

        }

        return;

    }


    /* =====================================================
       LATEST REPORT
    ===================================================== */

    const latest =
        reports[0];


    if (latestATS) {

        latestATS.textContent =
            formatScore(
                latest.ats_score
            );

    }


    if (latestMatch) {

        latestMatch.textContent =
            formatScore(
                latest.match_score
            );

    }


    /* =====================================================
       RENDER REPORT CARDS
    ===================================================== */

    if (reportList) {

        reportList.innerHTML =
            "";

        reports.forEach(
            report => {

                reportList.appendChild(
                    createReportCard(
                        report
                    )
                );

            }
        );

    }

}


/* =========================================================
   CREATE REPORT CARD
   ========================================================= */

function createReportCard(
    report
) {

    const card =
        document.createElement(
            "div"
        );


    card.className =
        "report-card";


    const reportId =
        report.id;


    const resumeId =
        report.resume ||
        report.resume_id ||
        "—";


    const title =
        report.report_title ||
        "AI Resume Analyzer Report";


    const status =
        report.status ||
        "Generated";


    const ats =
        formatScore(
            report.ats_score
        );


    const match =
        formatScore(
            report.match_score
        );


    const date =
        formatDate(
            report.generated_at
        );


    const statusClass =
        String(status)
            .toLowerCase();


    card.innerHTML = `

        <div class="report-card-main">

            <div class="report-icon">
                📄
            </div>


            <div class="report-details">

                <h3>
                    ${escapeHtml(title)}
                </h3>


                <p>
                    Report #${escapeHtml(reportId)}
                </p>


                <p>
                    Resume #${escapeHtml(resumeId)}
                </p>


                <span class="report-date">
                    ${escapeHtml(date)}
                </span>

            </div>

        </div>


        <div class="report-stats">

            <div class="report-stat">

                <span>
                    ATS Score
                </span>

                <strong>
                    ${ats}
                </strong>

            </div>


            <div class="report-stat">

                <span>
                    Match Score
                </span>

                <strong>
                    ${match}
                </strong>

            </div>


            <div class="report-stat">

                <span>
                    Status
                </span>

                <strong
                    class="status-badge ${escapeHtml(
                        statusClass
                    )}"
                >
                    ${escapeHtml(status)}
                </strong>

            </div>

        </div>


        <div class="report-actions">

            ${
                report.pdf_file
                    ? `

                        <a
                            class="report-button secondary"
                            href="${escapeHtml(
                                report.pdf_file
                            )}"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            View PDF
                        </a>

                    `
                    : ""
            }


            <button
                class="report-button primary"
                type="button"
                onclick="downloadReport(
                    ${reportId}
                )"
            >
                Download
            </button>


            <button
                class="report-button danger"
                type="button"
                onclick="deleteReport(
                    ${reportId}
                )"
            >
                Delete
            </button>

        </div>

    `;


    return card;

}


/* =========================================================
   GENERATE REPORT
   ========================================================= */

async function generateReport() {

    /*
     * IMPORTANT:
     *
     * Always read the resume ID at the moment
     * the Generate button is clicked.
     */

    const resumeId =
        getResumeId();


    console.log(
        "================================"
    );

    console.log(
        "GENERATE REPORT"
    );

    console.log(
        "RESUME ID:",
        resumeId
    );

    console.log(
        "================================"
    );


    /* =====================================================
       CHECK RESUME ID
    ===================================================== */

    if (!resumeId) {

        showMessage(
            "No resume found. Please upload a resume first.",
            "error"
        );

        return;

    }


    /* =====================================================
       VALIDATE RESUME ID
    ===================================================== */

    if (
        !/^\d+$/.test(
            String(resumeId)
        )
    ) {

        showMessage(
            "Invalid resume ID. Please upload your resume again.",
            "error"
        );

        return;

    }


    hideMessage();


    if (reportLoading) {

        reportLoading.style.display =
            "block";

    }


    if (generateReportButton) {

        generateReportButton.disabled =
            true;

        generateReportButton.innerHTML =
            "<span>Generating...</span>";

    }


    try {

        console.log(
            "CALLING:",
            `/reports/generate/${resumeId}/`
        );


        /*
         * Backend:
         *
         * GET /api/reports/generate/<resume_id>/
         */

        const response =
            await apiGet(
                `/reports/generate/${resumeId}/`
            );


        console.log(
            "GENERATED REPORT RESPONSE:",
            response
        );


        if (
            !response ||
            response.success === false
        ) {

            throw new Error(
                response?.message ||
                "Report generation failed."
            );

        }


        /*
         * Verify backend generated
         * the expected resume report.
         */

        if (
            response.resume_id &&
            String(
                response.resume_id
            ) !== String(
                resumeId
            )
        ) {

            console.warn(
                "RESUME ID MISMATCH:",
                {
                    requested:
                        resumeId,

                    generated:
                        response.resume_id
                }
            );

        }


        showMessage(
            `Report generated successfully for Resume #${resumeId}.`,
            "success"
        );


        /*
         * Reload history.
         */

        await loadReports();


        /*
         * Open generated PDF.
         */

        if (response.pdf_url) {

            window.open(
                response.pdf_url,
                "_blank"
            );

        }

    }

    catch (error) {

        console.error(
            "REPORT GENERATION ERROR:",
            error
        );


        showMessage(
            error.message ||
            "Unable to generate report.",
            "error"
        );

    }

    finally {

        if (reportLoading) {

            reportLoading.style.display =
                "none";

        }


        if (generateReportButton) {

            generateReportButton.disabled =
                false;

            generateReportButton.innerHTML =
                "<span>Generate Report</span>";

        }

    }

}


/* =========================================================
   DOWNLOAD REPORT
   ========================================================= */

async function downloadReport(
    reportId
) {

    try {

        console.log(
            "OPENING REPORT:",
            reportId
        );


        const response =
            await apiGet(
                `/reports/${reportId}/`
            );


        console.log(
            "REPORT DETAIL:",
            response
        );


        const report =
            response.report ||
            response.data ||
            response;


        if (
            !report ||
            !report.pdf_file
        ) {

            showMessage(
                "PDF file is not available for this report.",
                "error"
            );

            return;

        }


        /*
         * Open saved PDF.
         */

        window.open(
            report.pdf_file,
            "_blank"
        );

    }

    catch (error) {

        console.error(
            "DOWNLOAD ERROR:",
            error
        );


        showMessage(
            error.message ||
            "Unable to open report.",
            "error"
        );

    }

}


/* =========================================================
   DELETE REPORT
   ========================================================= */

async function deleteReport(
    reportId
) {

    const confirmed =
        window.confirm(
            "Are you sure you want to delete this report?"
        );


    if (!confirmed) {

        return;

    }


    try {

        console.log(
            "DELETING REPORT:",
            reportId
        );


        const response =
            await apiDelete(
                `/reports/${reportId}/delete/`
            );


        console.log(
            "DELETE RESPONSE:",
            response
        );


        showMessage(
            "Report deleted successfully.",
            "success"
        );


        await loadReports();

    }

    catch (error) {

        console.error(
            "DELETE REPORT ERROR:",
            error
        );


        showMessage(
            error.message ||
            "Unable to delete report.",
            "error"
        );

    }

}


/* =========================================================
   FORMAT SCORE
   ========================================================= */

function formatScore(
    score
) {

    if (
        score === null ||
        score === undefined ||
        score === ""
    ) {

        return "—";

    }


    return `${score}%`;

}


/* =========================================================
   FORMAT DATE
   ========================================================= */

function formatDate(
    value
) {

    if (!value) {

        return "Date unavailable";

    }


    try {

        return new Date(
            value
        ).toLocaleString();

    }

    catch {

        return String(
            value
        );

    }

}


/* =========================================================
   ESCAPE HTML
   ========================================================= */

function escapeHtml(
    value
) {

    return String(
        value ?? ""
    )
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
   GENERATE BUTTON
   ========================================================= */

if (generateReportButton) {

    generateReportButton.addEventListener(
        "click",
        generateReport
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
    "================================"
);

console.log(
    "REPORTS.JS LOADED"
);

console.log(
    "STORED RESUME ID:",
    localStorage.getItem(
        "resume_id"
    )
);

console.log(
    "================================"
);


loadUser();

loadReports();