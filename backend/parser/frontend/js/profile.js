/* =========================================================
   RESUME AI - PROFILE
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

const profileForm =
    document.getElementById(
        "profileForm"
    );

const fullNameInput =
    document.getElementById(
        "fullName"
    );

const emailInput =
    document.getElementById(
        "email"
    );

const phoneInput =
    document.getElementById(
        "phone"
    );

const profileMessage =
    document.getElementById(
        "profileMessage"
    );

const saveProfileButton =
    document.getElementById(
        "saveProfileButton"
    );

const profileAvatar =
    document.getElementById(
        "profileAvatar"
    );

const profileDisplayName =
    document.getElementById(
        "profileDisplayName"
    );

const profileDisplayEmail =
    document.getElementById(
        "profileDisplayEmail"
    );

const topbarAvatar =
    document.getElementById(
        "topbarAvatar"
    );

const topbarUserName =
    document.getElementById(
        "topbarUserName"
    );

const topbarUserEmail =
    document.getElementById(
        "topbarUserEmail"
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


/* =========================================================
   SHOW MESSAGE
   ========================================================= */

function showMessage(
    message,
    type
) {

    profileMessage.textContent =
        message;

    profileMessage.className =
        `profile-message ${type}`;

    profileMessage.style.display =
        "block";

}


/* =========================================================
   HIDE MESSAGE
   ========================================================= */

function hideMessage() {

    profileMessage.style.display =
        "none";

}


/* =========================================================
   SET USER UI
   ========================================================= */

function updateUserUI(user) {

    const name =
        user.full_name ||
        "User";

    const email =
        user.email ||
        "";

    const firstLetter =
        name
            .trim()
            .charAt(0)
            .toUpperCase() ||
        "U";


    /* Form */

    fullNameInput.value =
        name;

    emailInput.value =
        email;

    phoneInput.value =
        user.phone ||
        "";


    /* Profile card */

    profileDisplayName.textContent =
        name;

    profileDisplayEmail.textContent =
        email;

    profileAvatar.textContent =
        firstLetter;


    /* Topbar */

    topbarAvatar.textContent =
        firstLetter;

    topbarUserName.textContent =
        name;

    topbarUserEmail.textContent =
        email;

}


/* =========================================================
   LOAD PROFILE
   ========================================================= */

async function loadProfile() {

    try {

        console.log(
            "LOADING PROFILE..."
        );


        const response =
            await apiGet(
                "/users/profile/"
            );


        console.log(
            "PROFILE RESPONSE:",
            response
        );


        updateUserUI(
            response
        );

    }

    catch (error) {

        console.error(
            "PROFILE LOAD ERROR:",
            error
        );


        showMessage(
            error.message ||
            "Unable to load profile.",
            "error"
        );

    }

}


/* =========================================================
   UPDATE PROFILE
   ========================================================= */

profileForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        hideMessage();


        const fullName =
            fullNameInput.value.trim();

        const phone =
            phoneInput.value.trim();


        if (!fullName) {

            showMessage(
                "Full name is required.",
                "error"
            );

            return;

        }


        /* Disable button */

        saveProfileButton.disabled =
            true;

        saveProfileButton.textContent =
            "Saving...";


        try {

            console.log(
                "UPDATING PROFILE..."
            );


            const response =
                await apiPut(
                    "/users/profile/",
                    {
                        full_name:
                            fullName,

                        phone:
                            phone
                    }
                );


            console.log(
                "PROFILE UPDATE RESPONSE:",
                response
            );


            /*
             * Backend response:
             *
             * {
             *   success: true,
             *   message: "...",
             *   data: {...}
             * }
             */


            const updatedUser =
                response.data ||
                response;


            updateUserUI(
                updatedUser
            );


            showMessage(
                response.message ||
                "Profile updated successfully.",
                "success"
            );

        }

        catch (error) {

            console.error(
                "PROFILE UPDATE ERROR:",
                error
            );


            showMessage(
                error.message ||
                "Unable to update profile.",
                "error"
            );

        }

        finally {

            saveProfileButton.disabled =
                false;

            saveProfileButton.textContent =
                "Save Changes";

        }

    }
);


/* =========================================================
   LOGOUT
   ========================================================= */

logoutButton.addEventListener(
    "click",
    function () {

        logout();

    }
);


/* =========================================================
   MOBILE MENU
   ========================================================= */

menuButton.addEventListener(
    "click",
    function () {

        sidebar.classList.toggle(
            "open"
        );

    }
);


/* =========================================================
   INITIALIZE
   ========================================================= */

loadProfile();