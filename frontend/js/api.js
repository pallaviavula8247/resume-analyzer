/* =========================================================
   RESUME AI - API CONFIGURATION
   ========================================================= */

const API_BASE_URL =
    "http://127.0.0.1:8000/api";


/* =========================================================
   TOKEN FUNCTIONS
   ========================================================= */

function getAccessToken() {

    return localStorage.getItem(
        "access_token"
    );

}


function getRefreshToken() {

    return localStorage.getItem(
        "refresh_token"
    );

}


function saveTokens(
    access,
    refresh = null
) {

    if (access) {

        localStorage.setItem(
            "access_token",
            access
        );

    }

    if (refresh) {

        localStorage.setItem(
            "refresh_token",
            refresh
        );

    }

}


function clearTokens() {

    localStorage.removeItem(
        "access_token"
    );

    localStorage.removeItem(
        "refresh_token"
    );

}


function isAuthenticated() {

    return Boolean(
        getAccessToken()
    );

}


function logout() {

    clearTokens();

    window.location.href =
        "login.html";

}


/* =========================================================
   REFRESH ACCESS TOKEN
   Backend URL:

   POST /api/users/token/refresh/
   ========================================================= */

async function refreshAccessToken() {

    const refreshToken =
        getRefreshToken();


    if (!refreshToken) {

        console.warn(
            "NO REFRESH TOKEN FOUND"
        );

        return null;

    }


    try {

        console.log(
            "REFRESHING ACCESS TOKEN..."
        );


        const response =
            await fetch(
                `${API_BASE_URL}/users/token/refresh/`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        refresh:
                            refreshToken
                    })
                }
            );


        let data = null;


        try {

            data =
                await response.json();

        }

        catch {

            data = null;

        }


        if (!response.ok) {

            console.error(
                "REFRESH TOKEN FAILED:",
                response.status,
                data
            );

            return null;

        }


        if (!data || !data.access) {

            console.error(
                "NO ACCESS TOKEN IN REFRESH RESPONSE"
            );

            return null;

        }


        saveTokens(
            data.access,
            data.refresh || null
        );


        console.log(
            "TOKEN REFRESH SUCCESS"
        );


        return data.access;

    }

    catch (error) {

        console.error(
            "TOKEN REFRESH ERROR:",
            error
        );

        return null;

    }

}


/* =========================================================
   API REQUEST
   ========================================================= */

async function apiRequest(
    endpoint,
    options = {},
    retry = true
) {

    const token =
        getAccessToken();


    const headers = {
        ...(options.headers || {})
    };


    /*
     * IMPORTANT:
     *
     * Do NOT set Content-Type manually
     * when sending FormData.
     *
     * Browser automatically creates:
     *
     * multipart/form-data;
     * boundary=...
     */

    if (
        !(options.body instanceof FormData)
    ) {

        headers["Content-Type"] =
            "application/json";

    }


    if (token) {

        headers["Authorization"] =
            `Bearer ${token}`;

    }


    console.log(
        "API REQUEST:",
        endpoint
    );


    let response;


    try {

        response =
            await fetch(
                `${API_BASE_URL}${endpoint}`,
                {
                    ...options,
                    headers
                }
            );

    }

    catch (error) {

        console.error(
            "NETWORK ERROR:",
            error
        );

        throw new Error(
            "Unable to connect to the server. Make sure Django is running."
        );

    }


    /* =====================================================
       READ RESPONSE
       ===================================================== */

    let data = null;


    try {

        data =
            await response.json();

    }

    catch {

        data = null;

    }


    /* =====================================================
       ACCESS TOKEN EXPIRED
       ===================================================== */

    if (
        response.status === 401 &&
        retry
    ) {

        console.warn(
            "ACCESS TOKEN EXPIRED."
        );

        console.log(
            "TRYING REFRESH TOKEN..."
        );


        const newAccessToken =
            await refreshAccessToken();


        /*
         * Refresh successful
         */

        if (newAccessToken) {

            console.log(
                "RETRYING API REQUEST:",
                endpoint
            );


            const retryHeaders = {
                ...(options.headers || {})
            };


            if (
                !(options.body instanceof FormData)
            ) {

                retryHeaders[
                    "Content-Type"
                ] =
                    "application/json";

            }


            retryHeaders[
                "Authorization"
            ] =
                `Bearer ${newAccessToken}`;


            let retryResponse;


            try {

                retryResponse =
                    await fetch(
                        `${API_BASE_URL}${endpoint}`,
                        {
                            ...options,
                            headers:
                                retryHeaders
                        }
                    );

            }

            catch (error) {

                console.error(
                    "RETRY NETWORK ERROR:",
                    error
                );

                throw new Error(
                    "Unable to connect to the server."
                );

            }


            let retryData = null;


            try {

                retryData =
                    await retryResponse.json();

            }

            catch {

                retryData = null;

            }


            console.log(
                "RETRY STATUS:",
                retryResponse.status
            );


            /*
             * Retry successful
             */

            if (
                retryResponse.ok
            ) {

                return retryData;

            }


            /*
             * Refresh worked but
             * retry still returned 401.
             */

            if (
                retryResponse.status === 401
            ) {

                clearTokens();

                throw new Error(
                    "Session expired. Please login again."
                );

            }


            throw new Error(
                getApiErrorMessage(
                    retryData
                )
            );

        }


        /*
         * Refresh token failed.
         */

        clearTokens();

        throw new Error(
            "Session expired. Please login again."
        );

    }


    /* =====================================================
       OTHER API ERRORS
       ===================================================== */

    if (!response.ok) {

        console.error(
            "API ERROR:",
            response.status,
            data
        );


        throw new Error(
            getApiErrorMessage(
                data
            )
        );

    }


    /* =====================================================
       SUCCESS
       ===================================================== */

    return data;

}


/* =========================================================
   API ERROR MESSAGE
   ========================================================= */

function getApiErrorMessage(
    data
) {

    if (!data) {

        return "Something went wrong.";

    }


    if (data.message) {

        return data.message;

    }


    if (data.detail) {

        return data.detail;

    }


    if (data.error) {

        return data.error;

    }


    if (data.errors) {

        return flattenErrors(
            data.errors
        );

    }


    if (
        typeof data === "object"
    ) {

        return flattenErrors(
            data
        );

    }


    return "Something went wrong.";

}


/* =========================================================
   FLATTEN DJANGO VALIDATION ERRORS
   ========================================================= */

function flattenErrors(
    errors
) {

    try {

        return Object.values(
            errors
        )
            .flat()
            .map(
                item => String(item)
            )
            .join(" ");

    }

    catch {

        return "Something went wrong.";

    }

}


/* =========================================================
   GET
   ========================================================= */

async function apiGet(
    endpoint
) {

    return apiRequest(
        endpoint,
        {
            method: "GET"
        }
    );

}


/* =========================================================
   POST JSON
   ========================================================= */

async function apiPost(
    endpoint,
    data = {}
) {

    return apiRequest(
        endpoint,
        {
            method: "POST",

            body:
                JSON.stringify(data)
        }
    );

}


/* =========================================================
   POST FORM DATA
   ========================================================= */

async function apiPostForm(
    endpoint,
    formData
) {

    return apiRequest(
        endpoint,
        {
            method: "POST",

            body: formData
        }
    );

}


/* =========================================================
   PUT
   ========================================================= */

async function apiPut(
    endpoint,
    data = {}
) {

    return apiRequest(
        endpoint,
        {
            method: "PUT",

            body:
                JSON.stringify(data)
        }
    );

}


/* =========================================================
   DELETE
   ========================================================= */

async function apiDelete(
    endpoint
) {

    return apiRequest(
        endpoint,
        {
            method: "DELETE"
        }
    );

}