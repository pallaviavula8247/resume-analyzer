/* =========================================================
   RESUME AI - RECOMMENDATIONS
   ========================================================= */

if (!isAuthenticated()) {
    window.location.href = "login.html";
}


/* =========================================================
   ELEMENTS
   ========================================================= */

const loading =
    document.getElementById("recommendationLoading");

const errorBox =
    document.getElementById("recommendationError");

const content =
    document.getElementById("recommendationContent");


/* =========================================================
   LOAD RECOMMENDATIONS
   ========================================================= */

async function loadRecommendations() {

    const resumeId =
        localStorage.getItem("resume_id");

    console.log(
        "RECOMMENDATION RESUME ID:",
        resumeId
    );


    if (!resumeId) {

        showError(
            "No resume found. Please upload your resume first."
        );

        return;
    }


    try {

        loading.style.display = "block";
        content.style.display = "none";
        errorBox.style.display = "none";


        console.log(
            "REQUESTING RECOMMENDATIONS:",
            `/recommendation/${resumeId}/`
        );


        const response =
            await apiGet(
                `/recommendation/${resumeId}/`
            );


        console.log(
            "RECOMMENDATION RESPONSE:",
            response
        );


        loading.style.display = "none";


        renderRecommendations(response);


    }

    catch (error) {

        console.error(
            "RECOMMENDATION ERROR:",
            error
        );

        loading.style.display = "none";

        showError(
            error.message ||
            "Unable to load recommendations."
        );

    }

}


/* =========================================================
   RENDER
   ========================================================= */

function renderRecommendations(response) {

    let recommendations = null;


    /*
     * Your backend may return:
     *
     * data: [...]
     *
     * or
     *
     * data: {
     *     recommendations: [...]
     * }
     */


    if (
        Array.isArray(response?.data)
    ) {

        recommendations =
            response.data;

    }

    else if (
        Array.isArray(
            response?.data?.recommendations
        )
    ) {

        recommendations =
            response.data.recommendations;

    }

    else if (
        Array.isArray(
            response?.recommendations
        )
    ) {

        recommendations =
            response.recommendations;

    }


    console.log(
        "RECOMMENDATIONS:",
        recommendations
    );


    if (
        !recommendations ||
        recommendations.length === 0
    ) {

        content.innerHTML = `
            <div class="empty-recommendations">
                <div class="empty-icon">✦</div>

                <h2>No recommendations available</h2>

                <p>
                    Upload and analyze your resume to receive
                    personalized AI recommendations.
                </p>
            </div>
        `;

        content.style.display = "block";

        return;
    }


    content.innerHTML =
        recommendations
            .map(
                (recommendation, index) =>
                    createRecommendationCard(
                        recommendation,
                        index
                    )
            )
            .join("");


    content.style.display =
        "grid";
}


/* =========================================================
   CARD
   ========================================================= */

function createRecommendationCard(
    recommendation,
    index
) {

    let title =
        `Recommendation ${index + 1}`;

    let description =
        "";


    if (
        typeof recommendation ===
        "string"
    ) {

        description =
            recommendation;

    }

    else if (
        typeof recommendation ===
        "object"
    ) {

        title =
            recommendation.title ||
            recommendation.category ||
            recommendation.type ||
            title;

        description =
            recommendation.description ||
            recommendation.recommendation ||
            recommendation.message ||
            recommendation.text ||
            JSON.stringify(
                recommendation
            );

    }


    return `
        <article class="recommendation-card">

            <div class="recommendation-number">
                ${String(index + 1).padStart(2, "0")}
            </div>

            <div class="recommendation-body">

                <h3>
                    ${escapeHtml(title)}
                </h3>

                <p>
                    ${escapeHtml(description)}
                </p>

            </div>

        </article>
    `;
}


/* =========================================================
   ERROR
   ========================================================= */

function showError(message) {

    errorBox.textContent =
        message;

    errorBox.style.display =
        "block";

}


/* =========================================================
   HTML SAFETY
   ========================================================= */

function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


/* =========================================================
   START
   ========================================================= */

loadRecommendations();