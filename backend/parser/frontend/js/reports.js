/* =========================================================
   RESUME AI - REPORTS JAVASCRIPT
   ========================================================= */


/* =========================================================
   PAGE STATE
   ========================================================= */

let reports = [];

let currentResumeId = null;


/* =========================================================
   DOM ELEMENTS
   ========================================================= */

const reportsContainer =
    document.getElementById("reportsContainer");

const reportLoading =
    document.getElementById("reportLoading");

const reportError =
    document.getElementById("reportError");

const reportEmpty =
    document.getElementById("reportEmpty");

const generateReportButton =
    document.getElementById("generateReportButton");


/* =========================================================
   SHOW / HIDE HELPERS
   ========================================================= */

function showLoading() {

    if (reportLoading) {

        reportLoading.style.display = "flex";

    }

}


function hideLoading() {

    if (reportLoading) {

        reportLoading.style.display = "none";

    }

}


function showError(message) {

    if (!reportError) {
        return;
    }

    reportError.textContent =
        message || "Something went wrong.";

    reportError.style.display =
        "block";

}


function hideError() {

    if (reportError) {

        reportError.style.display =
            "none";

    }

}


/* =========================================================
   GET RESUME ID
   ========================================================= */

async function getResumeId() {

    try {

        console.log(
            "GETTING USER PROFILE..."
        );

        const profile =
            await apiGet(
                "/users/profile/"
            );

        console.log(
            "PROFILE:",
            profile
        );

        /*
         * Different possible backend
         * response structures.
         */

        const resumeId =
            profile?.resume_id ||
            profile?.latest_resume_id ||
            profile?.data?.resume_id ||
            profile?.data?.latest_resume_id ||
            profile?.profile?.resume_id ||
            profile?.user?.resume_id;

        if (resumeId) {

            currentResumeId =
                resumeId;

            console.log(
                "RESUME ID:",
                currentResumeId
            );

            return currentResumeId;

        }

        /*
         * If profile does not contain
         * resume_id, try resume list.
         */

        try {

            const resumes =
                await apiGet(
                    "/parser/resumes/"
                );

            console.log(
                "RESUMES:",
                resumes
            );

            let resumeList = [];

            if (
                Array.isArray(resumes)
            ) {

                resumeList =
                    resumes;

            }

            else if (
                Array.isArray(
                    resumes?.resumes
                )
            ) {

                resumeList =
                    resumes.resumes;

            }

            else if (
                Array.isArray(
                    resumes?.data
                )
            ) {

                resumeList =
                    resumes.data;

            }

            if (
                resumeList.length > 0
            ) {

                currentResumeId =
                    resumeList[
                        resumeList.length - 1
                    ].id;

                console.log(
                    "LATEST RESUME ID:",
                    currentResumeId
                );

                return currentResumeId;

            }

        }

        catch (resumeError) {

            console.warn(
                "RESUME LIST API NOT AVAILABLE:",
                resumeError
            );

        }

        throw new Error(
            "No uploaded resume found. Please upload a resume first."
        );

    }

    catch (error) {

        console.error(
            "GET RESUME ID ERROR:",
            error
        );

        throw error;

    }

}


/* =========================================================
   LOAD REPORTS
   ========================================================= */

async function loadReports() {

    hideError();

    showLoading();

    if (reportsContainer) {

        reportsContainer.innerHTML = "";

    }

    try {

        console.log(
            "LOADING REPORTS..."
        );

        const response =
            await apiGet(
                "/reports/"
            );

        console.log(
            "REPORTS RESPONSE:",
            response
        );

        /*
         * Backend returns:
         *
         * {
         *   success: true,
         *   count: ...,
         *   reports: [...]
         * }
         */

        if (
            Array.isArray(
                response?.reports
            )
        ) {

            reports =
                response.reports;

        }

        else if (
            Array.isArray(response)
        ) {

            reports =
                response;

        }

        else {

            reports = [];

        }

        hideLoading();

        renderReports();

    }

    catch (error) {

        hideLoading();

        console.error(
            "LOAD REPORTS ERROR:",
            error
        );

        showError(
            error.message ||
            "Unable to load reports."
        );

    }

}


/* =========================================================
   RENDER REPORTS
   ========================================================= */

function renderReports() {

    if (!reportsContainer) {
        return;
    }

    reportsContainer.innerHTML = "";

    if (
        !reports ||
        reports.length === 0
    ) {

        if (reportEmpty) {

            reportEmpty.style.display =
                "block";

        }

        return;

    }

    if (reportEmpty) {

        reportEmpty.style.display =
            "none";

    }


    reports.forEach(
        report => {

            const card =
                createReportCard(
                    report
                );

            reportsContainer.appendChild(
                card
            );

        }
    );

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
        report.id ||
        report.report_id ||
        "—";


    const resumeId =
        report.resume_id ||
        report.resume ||
        "—";


    const atsScore =
        report.ats_score ??
        0;


    const matchScore =
        report.match_score ??
        0;


    const title =
        report.report_title ||
        report.title ||
        "AI Resume Analyzer Report";


    const status =
        report.status ||
        "Generated";


    const generatedAt =
        report.generated_at ||
        report.created_at ||
        report.uploaded_at;


    const formattedDate =
        formatDate(
            generatedAt
        );


    const pdfUrl =
        report.pdf_url ||
        report.pdf_file_url ||
        report.pdf_file;


    card.innerHTML = `

        <div class="report-card-header">

            <div>

                <span class="report-label">
                    RESUME REPORT
                </span>

                <h3>
                    ${escapeHtml(title)}
                </h3>

            </div>

            <span class="report-status">
                ${escapeHtml(status)}
            </span>

        </div>


        <div class="report-card-body">

            <div class="report-score">

                <span class="score-value">
                    ${escapeHtml(atsScore)}
                </span>

                <span class="score-label">
                    ATS Score
                </span>

            </div>


            <div class="report-score">

                <span class="score-value">
                    ${escapeHtml(matchScore)}
                </span>

                <span class="score-label">
                    Match Score
                </span>

            </div>


            <div class="report-info">

                <span>
                    Report ID
                </span>

                <strong>
                    #${escapeHtml(reportId)}
                </strong>

            </div>


            <div class="report-info">

                <span>
                    Resume ID
                </span>

                <strong>
                    ${escapeHtml(resumeId)}
                </strong>

            </div>


            <div class="report-info">

                <span>
                    Generated
                </span>

                <strong>
                    ${escapeHtml(formattedDate)}
                </strong>

            </div>

        </div>


        <div class="report-card-actions">

            ${
                pdfUrl
                ?
                `
                <button
                    type="button"
                    class="report-button primary"
                    onclick="openReportPDF('${escapeAttribute(pdfUrl)}')"
                >
                    View PDF
                </button>
                `
                :
                ""
            }


            <button
                type="button"
                class="report-button secondary"
                onclick="downloadReport('${escapeAttribute(pdfUrl || "")}', ${Number(resumeId) || 0})"
            >
                Download
            </button>


            <button
                type="button"
                class="report-button danger"
                onclick="deleteReport(${Number(reportId) || 0})"
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

    hideError();

    try {

        if (
            generateReportButton
        ) {

            generateReportButton.disabled =
                true;

            generateReportButton.textContent =
                "Generating...";

        }


        /*
         * Get latest resume ID.
         */

        const resumeId =
            await getResumeId();


        if (!resumeId) {

            throw new Error(
                "Resume ID not found."
            );

        }


        console.log(
            "GENERATING REPORT FOR RESUME:",
            resumeId
        );


        /*
         * IMPORTANT:
         *
         * Backend ReportGenerateView
         * uses GET.
         *
         * Therefore we use apiGet().
         *
         * NOT apiPost().
         */

        const response =
            await apiGet(
                `/reports/generate/${resumeId}/`
            );


        console.log(
            "GENERATE REPORT RESPONSE:",
            response
        );


        if (
            !response ||
            response.success !== true
        ) {

            throw new Error(
                response?.message ||
                "Report generation failed."
            );

        }


        /*
         * Reload report history.
         */

        await loadReports();


        /*
         * Open generated PDF if available.
         */

        if (
            response.pdf_url
        ) {

            window.open(
                response.pdf_url,
                "_blank"
            );

        }


        alert(
            "Report generated successfully."
        );

    }

    catch (error) {

        console.error(
            "GENERATE REPORT ERROR:",
            error
        );

        showError(
            error.message ||
            "Unable to generate report."
        );

    }

    finally {

        if (
            generateReportButton
        ) {

            generateReportButton.disabled =
                false;

            generateReportButton.textContent =
                "Generate Report";

        }

    }

}


/* =========================================================
   OPEN PDF
   ========================================================= */

function openReportPDF(
    pdfUrl
) {

    if (!pdfUrl) {

        alert(
            "PDF is not available."
        );

        return;

    }

    window.open(
        pdfUrl,
        "_blank"
    );

}


/* =========================================================
   DOWNLOAD REPORT
   ========================================================= */

async function downloadReport(
    pdfUrl,
    resumeId
) {

    try {

        /*
         * If database already provides
         * PDF URL, use it.
         */

        if (pdfUrl) {

            const link =
                document.createElement(
                    "a"
                );

            link.href =
                pdfUrl;

            link.target =
                "_blank";

            link.click();

            return;

        }


        /*
         * Otherwise generate/download
         * through backend.
         */

        if (!resumeId) {

            throw new Error(
                "Resume ID not available."
            );

        }


        const token =
            getAccessToken();


        const response =
            await fetch(
                `${API_BASE_URL}/reports/${resumeId}/pdf/`,
                {
                    method: "GET",

                    headers: {

                        "Authorization":
                            `Bearer ${token}`

                    }
                }
            );


        if (!response.ok) {

            if (
                response.status === 401
            ) {

                throw new Error(
                    "Session expired. Please login again."
                );

            }

            throw new Error(
                "Unable to download PDF."
            );

        }


        const blob =
            await response.blob();


        const url =
            window.URL.createObjectURL(
                blob
            );


        const link =
            document.createElement(
                "a"
            );


        link.href =
            url;

        link.download =
            `resume_report_${resumeId}.pdf`;


        document.body.appendChild(
            link
        );


        link.click();


        link.remove();


        window.URL.revokeObjectURL(
            url
        );

    }

    catch (error) {

        console.error(
            "DOWNLOAD ERROR:",
            error
        );

        showError(
            error.message ||
            "Unable to download report."
        );

    }

}


/* =========================================================
   DELETE REPORT
   ========================================================= */

async function deleteReport(
    reportId
) {

    if (!reportId) {

        alert(
            "Invalid report ID."
        );

        return;

    }


    const confirmed =
        confirm(
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
            await apiRequest(
                `/reports/${reportId}/delete/`,
                {
                    method: "DELETE"
                }
            );


        console.log(
            "DELETE RESPONSE:",
            response
        );


        if (
            response?.success === false
        ) {

            throw new Error(
                response.message ||
                "Unable to delete report."
            );

        }


        await loadReports();


        alert(
            "Report deleted successfully."
        );

    }

    catch (error) {

        console.error(
            "DELETE REPORT ERROR:",
            error
        );

        showError(
            error.message ||
            "Unable to delete report."
        );

    }

}


/* =========================================================
   FORMAT DATE
   ========================================================= */

function formatDate(
    value
) {

    if (!value) {

        return "—";

    }


    try {

        const date =
            new Date(value);


        if (
            Number.isNaN(
                date.getTime()
            )
        ) {

            return String(value);

        }


        return date.toLocaleDateString(
            "en-IN",
            {
                day: "2-digit",
                month: "short",
                year: "numeric"
            }
        );

    }

    catch {

        return String(value);

    }

}


/* =========================================================
   HTML ESCAPE
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
   ATTRIBUTE ESCAPE
   ========================================================= */

function escapeAttribute(
    value
) {

    return String(
        value ?? ""
    )
        .replace(
            /\\/g,
            "\\\\"
        )
        .replace(
            /'/g,
            "\\'"
        );

}


/* =========================================================
   GENERATE BUTTON EVENT
   ========================================================= */

if (
    generateReportButton
) {

    generateReportButton.addEventListener(
        "click",
        generateReport
    );

}


/* =========================================================
   PAGE LOAD
   ========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    async () => {

        console.log(
            "REPORTS.JS LOADED"
        );

        /*
         * Check authentication.
         */

        if (
            !isAuthenticated()
        ) {

            window.location.href =
                "login.html";

            return;

        }


        /*
         * Load report history.
         */

        await loadReports();

    }
);