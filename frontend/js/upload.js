/* =========================================================
   RESUME AI - RESUME UPLOAD
   ========================================================= */

console.log("UPLOAD.JS LOADED");


/* =========================================================
   AUTH CHECK
   ========================================================= */

if (typeof isAuthenticated !== "function") {

    console.error("api.js is not loaded correctly.");

} else if (!isAuthenticated()) {

    window.location.href = "login.html";

}


/* =========================================================
   API
   ========================================================= */

const UPLOAD_URL =
    "http://127.0.0.1:8000/api/parser/upload/";

const MAX_FILE_SIZE =
    5 * 1024 * 1024;


/* =========================================================
   DOM
   ========================================================= */

const uploadForm =
    document.getElementById("uploadForm");

const resumeFile =
    document.getElementById("resumeFile");

const browseButton =
    document.getElementById("browseButton");

const dropZone =
    document.getElementById("dropZone");

const selectedFileBox =
    document.getElementById("selectedFile");

const fileName =
    document.getElementById("fileName");

const fileSize =
    document.getElementById("fileSize");

const removeFile =
    document.getElementById("removeFile");

const uploadButton =
    document.getElementById("uploadButton");

const uploadError =
    document.getElementById("uploadError");

const uploadSuccess =
    document.getElementById("uploadSuccess");

const progressContainer =
    document.getElementById("uploadProgressContainer");

const progressBar =
    document.getElementById("progressBar");

const progressText =
    document.getElementById("progressText");

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
   SELECTED FILE
   ========================================================= */

let selectedResume = null;


/* =========================================================
   BASIC DOM CHECK
   ========================================================= */

console.log("Upload form:", uploadForm);
console.log("File input:", resumeFile);
console.log("Upload button:", uploadButton);


/* =========================================================
   LOAD USER
   ========================================================= */

async function loadUser() {

    try {

        if (typeof apiGet !== "function") {

            console.error(
                "apiGet() is not available."
            );

            return;
        }

        const response =
            await apiGet("/users/profile/");

        console.log(
            "PROFILE:",
            response
        );

        const fullName =
            response.full_name || "User";

        const email =
            response.email || "";


        if (topbarUserName) {

            topbarUserName.textContent =
                fullName;

        }


        if (topbarUserEmail) {

            topbarUserEmail.textContent =
                email;

        }


        if (userAvatar) {

            userAvatar.textContent =
                fullName
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
   FILE SIZE
   ========================================================= */

function formatFileSize(bytes) {

    if (bytes < 1024) {

        return bytes + " B";

    }

    if (bytes < 1024 * 1024) {

        return (
            (bytes / 1024).toFixed(1)
            + " KB"
        );

    }

    return (
        (bytes / (1024 * 1024)).toFixed(2)
        + " MB"
    );

}


/* =========================================================
   CLEAR MESSAGE
   ========================================================= */

function clearMessages() {

    if (uploadError) {

        uploadError.style.display =
            "none";

        uploadError.textContent =
            "";

    }

    if (uploadSuccess) {

        uploadSuccess.style.display =
            "none";

        uploadSuccess.textContent =
            "";

    }

}


/* =========================================================
   SHOW ERROR
   ========================================================= */

function showError(message) {

    console.error(
        "UPLOAD ERROR:",
        message
    );


    if (uploadError) {

        uploadError.textContent =
            message;

        uploadError.style.display =
            "block";

    }


    if (uploadSuccess) {

        uploadSuccess.style.display =
            "none";

    }

}


/* =========================================================
   SHOW SUCCESS
   ========================================================= */

function showSuccess(message) {

    console.log(
        "UPLOAD SUCCESS:",
        message
    );


    if (uploadSuccess) {

        uploadSuccess.textContent =
            message;

        uploadSuccess.style.display =
            "block";

    }


    if (uploadError) {

        uploadError.style.display =
            "none";

    }

}


/* =========================================================
   RESET FILE
   ========================================================= */

function resetFile() {

    selectedResume = null;


    if (resumeFile) {

        resumeFile.value = "";

    }


    if (selectedFileBox) {

        selectedFileBox.style.display =
            "none";

    }


    if (uploadButton) {

        uploadButton.disabled =
            true;

    }

}


/* =========================================================
   HANDLE FILE
   ========================================================= */

function handleFile(file) {

    clearMessages();


    console.log(
        "HANDLE FILE:",
        file
    );


    if (!file) {

        console.log(
            "NO FILE SELECTED"
        );

        resetFile();

        return;

    }


    /* -----------------------------------------------------
       PDF CHECK
       ----------------------------------------------------- */

    const isPDF =
        file.type === "application/pdf" ||
        file.name
            .toLowerCase()
            .endsWith(".pdf");


    if (!isPDF) {

        showError(
            "Please select a PDF resume."
        );

        resetFile();

        return;

    }


    /* -----------------------------------------------------
       SIZE CHECK
       ----------------------------------------------------- */

    if (file.size > MAX_FILE_SIZE) {

        showError(
            "File size must be less than 5 MB."
        );

        resetFile();

        return;

    }


    /* -----------------------------------------------------
       SAVE FILE
       ----------------------------------------------------- */

    selectedResume =
        file;


    if (fileName) {

        fileName.textContent =
            file.name;

    }


    if (fileSize) {

        fileSize.textContent =
            formatFileSize(
                file.size
            );

    }


    if (selectedFileBox) {

        selectedFileBox.style.display =
            "flex";

    }


    if (uploadButton) {

        uploadButton.disabled =
            false;

    }


    console.log(
        "FILE READY:",
        selectedResume.name,
        selectedResume.size
    );

}


/* =========================================================
   BROWSE
   ========================================================= */

if (browseButton) {

    browseButton.addEventListener(
        "click",
        function () {

            console.log(
                "BROWSE BUTTON CLICKED"
            );

            resumeFile.click();

        }
    );

}


/* =========================================================
   FILE INPUT
   ========================================================= */

if (resumeFile) {

    resumeFile.addEventListener(
        "change",
        function (event) {

            console.log(
                "INPUT CHANGE EVENT"
            );


            console.log(
                "FILES:",
                event.target.files
            );


            const file =
                event.target.files[0];


            handleFile(file);

        }
    );

}


/* =========================================================
   DRAG & DROP
   ========================================================= */

if (dropZone) {

    dropZone.addEventListener(
        "dragover",
        function (event) {

            event.preventDefault();

            dropZone.classList.add(
                "drag-over"
            );

        }
    );


    dropZone.addEventListener(
        "dragleave",
        function () {

            dropZone.classList.remove(
                "drag-over"
            );

        }
    );


    dropZone.addEventListener(
        "drop",
        function (event) {

            event.preventDefault();


            dropZone.classList.remove(
                "drag-over"
            );


            const file =
                event
                    .dataTransfer
                    .files[0];


            console.log(
                "DROPPED FILE:",
                file
            );


            if (!file) {

                return;

            }


            /*
             * Put dropped file into
             * the real input.
             */

            try {

                const dataTransfer =
                    new DataTransfer();

                dataTransfer.items.add(
                    file
                );

                resumeFile.files =
                    dataTransfer.files;

            }

            catch (error) {

                console.error(
                    "DATA TRANSFER ERROR:",
                    error
                );

            }


            handleFile(file);

        }
    );

}


/* =========================================================
   REMOVE FILE
   ========================================================= */

if (removeFile) {

    removeFile.addEventListener(
        "click",
        function () {

            resetFile();

            clearMessages();

        }
    );

}


/* =========================================================
   UPLOAD
   ========================================================= */

if (uploadForm) {

    uploadForm.addEventListener(
        "submit",
        function (event) {

            event.preventDefault();


            console.log(
                "================================="
            );

            console.log(
                "SUBMIT EVENT FIRED"
            );

            console.log(
                "================================="
            );


            clearMessages();


            /* -------------------------------------------------
               FILE CHECK
               ------------------------------------------------- */

            if (
                !resumeFile ||
                !resumeFile.files ||
                resumeFile.files.length === 0
            ) {

                console.error(
                    "NO FILE SELECTED"
                );

                showError(
                    "Please select a resume PDF first."
                );

                return;

            }


            const file =
                resumeFile.files[0];


            console.log(
                "UPLOADING FILE:",
                file.name
            );

            console.log(
                "FILE SIZE:",
                file.size
            );

            console.log(
                "FILE TYPE:",
                file.type
            );


            /* -------------------------------------------------
               TOKEN
               ------------------------------------------------- */

            if (
                typeof getAccessToken !==
                "function"
            ) {

                showError(
                    "Authentication helper is missing from api.js."
                );

                return;

            }


            const token =
                getAccessToken();


            console.log(
                "TOKEN EXISTS:",
                !!token
            );


            if (!token) {

                showError(
                    "Your session has expired. Please login again."
                );

                setTimeout(
                    function () {

                        window.location.href =
                            "login.html";

                    },
                    1500
                );

                return;

            }


            /* -------------------------------------------------
               FORM DATA
               ------------------------------------------------- */

            const formData =
                new FormData();


            formData.append(
                "resume_file",
                file
            );


            console.log(
                "FORM DATA:",
                formData.get(
                    "resume_file"
                )
            );


            /* -------------------------------------------------
               BUTTON
               ------------------------------------------------- */

            uploadButton.disabled =
                true;

            uploadButton.textContent =
                "Uploading...";


            /* -------------------------------------------------
               PROGRESS
               ------------------------------------------------- */

            if (progressContainer) {

                progressContainer.style.display =
                    "block";

            }


            if (progressBar) {

                progressBar.style.width =
                    "0%";

            }


            if (progressText) {

                progressText.textContent =
                    "0%";

            }


            /* -------------------------------------------------
               XHR
               ------------------------------------------------- */

            const xhr =
                new XMLHttpRequest();


            xhr.open(
                "POST",
                UPLOAD_URL,
                true
            );


            /*
             * JWT authentication
             */

            xhr.setRequestHeader(
                "Authorization",
                "Bearer " + token
            );


            /*
             * IMPORTANT:
             *
             * DO NOT set Content-Type manually.
             *
             * Browser automatically creates:
             *
             * multipart/form-data;
             * boundary=...
             *
             */


            /* -------------------------------------------------
               PROGRESS
               ------------------------------------------------- */

            xhr.upload.addEventListener(
                "progress",
                function (event) {

                    if (
                        !event.lengthComputable
                    ) {

                        return;

                    }


                    const percent =
                        Math.round(
                            (
                                event.loaded /
                                event.total
                            ) * 100
                        );


                    if (progressBar) {

                        progressBar.style.width =
                            percent + "%";

                    }


                    if (progressText) {

                        progressText.textContent =
                            percent + "%";

                    }


                    console.log(
                        "UPLOAD PROGRESS:",
                        percent + "%"
                    );

                }
            );


            /* -------------------------------------------------
               RESPONSE
               ------------------------------------------------- */

            xhr.onload =
                function () {

                    console.log(
                        "================================="
                    );

                    console.log(
                        "UPLOAD STATUS:",
                        xhr.status
                    );

                    console.log(
                        "UPLOAD RESPONSE:",
                        xhr.responseText
                    );

                    console.log(
                        "================================="
                    );


                    let responseData;


                    try {

                        responseData =
                            JSON.parse(
                                xhr.responseText
                            );

                    }

                    catch (error) {

                        console.error(
                            "JSON PARSE ERROR:",
                            error
                        );

                        responseData = null;

                    }


                    /* =========================================
                       SUCCESS
                       ========================================= */

                    if (
                        xhr.status >= 200 &&
                        xhr.status < 300
                    ) {

                        if (progressBar) {

                            progressBar.style.width =
                                "100%";

                        }


                        if (progressText) {

                            progressText.textContent =
                                "100%";

                        }


                        if (progressContainer) {

                            progressContainer.style.display =
                                "block";

                        }


                        uploadButton.textContent =
                            "Upload Successful";


                        showSuccess(
                            responseData &&
                            responseData.message
                                ? responseData.message
                                : "Resume uploaded successfully."
                        );


                        console.log(
                            "FULL SUCCESS RESPONSE:",
                            responseData
                        );


                        /* -----------------------------------------
                           SAVE RESUME ID
                           ----------------------------------------- */

                        if (
                            responseData &&
                            responseData.data &&
                            responseData.data.resume_id
                        ) {

                            localStorage.setItem(
                                "resume_id",
                                responseData
                                    .data
                                    .resume_id
                            );

                            console.log(
                                "RESUME ID SAVED:",
                                responseData
                                    .data
                                    .resume_id
                            );

                        }


                        /* -----------------------------------------
                           SAVE PARSED DATA
                           ----------------------------------------- */

                        if (
                            responseData &&
                            responseData.data &&
                            responseData.data.parsed_data
                        ) {

                            localStorage.setItem(
                                "parsed_resume",
                                JSON.stringify(
                                    responseData
                                        .data
                                        .parsed_data
                                )
                            );

                        }


                        /*
                         * IMPORTANT:
                         *
                         * Do NOT redirect automatically yet.
                         *
                         * First confirm upload works.
                         */

                        uploadButton.disabled =
                            false;


                        return;

                    }


                    /* =========================================
                       ERROR
                       ========================================= */

                    let message =
                        "Resume upload failed.";


                    if (
                        responseData &&
                        responseData.message
                    ) {

                        message =
                            responseData.message;

                    }


                    if (
                        responseData &&
                        responseData.error
                    ) {

                        message =
                            responseData.error;

                    }


                    if (
                        responseData &&
                        responseData.errors
                    ) {

                        const errors =
                            responseData.errors;


                        message =
                            Object.keys(errors)
                                .map(
                                    function (key) {

                                        return (
                                            key +
                                            ": " +
                                            errors[key]
                                        );

                                    }
                                )
                                .join(" ");

                    }


                    showError(
                        message
                    );


                    uploadButton.disabled =
                        false;

                    uploadButton.textContent =
                        "Upload & Analyze Resume";


                    if (progressContainer) {

                        progressContainer.style.display =
                            "none";

                    }

                };


            /* -------------------------------------------------
               NETWORK ERROR
               ------------------------------------------------- */

            xhr.onerror =
                function () {

                    console.error(
                        "NETWORK ERROR"
                    );


                    showError(
                        "Cannot connect to Django server. Make sure the backend is running."
                    );


                    uploadButton.disabled =
                        false;


                    uploadButton.textContent =
                        "Upload & Analyze Resume";


                    if (progressContainer) {

                        progressContainer.style.display =
                            "none";

                    }

                };


            /* -------------------------------------------------
               TIMEOUT
               ------------------------------------------------- */

            xhr.ontimeout =
                function () {

                    console.error(
                        "UPLOAD TIMEOUT"
                    );


                    showError(
                        "Upload timed out. Please try again."
                    );


                    uploadButton.disabled =
                        false;


                    uploadButton.textContent =
                        "Upload & Analyze Resume";

                };


            xhr.timeout =
                120000;


            /* -------------------------------------------------
               SEND
               ------------------------------------------------- */

            console.log(
                "SENDING REQUEST TO:",
                UPLOAD_URL
            );


            xhr.send(
                formData
            );

        }
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

            } else {

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
   INITIALIZE
   ========================================================= */

loadUser();