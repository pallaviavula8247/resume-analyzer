/* =========================================================
   RESUME AI - DASHBOARD
   ========================================================= */


/* =========================================================
   AUTH CHECK
   ========================================================= */

if (!isAuthenticated()) {

    window.location.href =
        "login.html";
}


/* =========================================================
   ELEMENTS
   ========================================================= */

const welcomeName =
    document.getElementById("welcomeName");

const topbarUserName =
    document.getElementById("topbarUserName");

const topbarUserEmail =
    document.getElementById("topbarUserEmail");

const userAvatar =
    document.getElementById("userAvatar");

const logoutButton =
    document.getElementById("logoutButton");

const menuButton =
    document.getElementById("menuButton");

const sidebar =
    document.getElementById("sidebar");


/* =========================================================
   LOAD PROFILE
   ========================================================= */

async function loadProfile() {

    try {

        const user =
            await apiGet(
                "/users/profile/"
            );


        console.log(
            "PROFILE RESPONSE:",
            user
        );


        /*
         * Display full name.
         */

        const fullName =
            user.full_name ||
            "User";


        welcomeName.textContent =
            fullName;

        topbarUserName.textContent =
            fullName;


        /*
         * Display email.
         */

        topbarUserEmail.textContent =
            user.email ||
            "";


        /*
         * Create avatar from first
         * character of name.
         */

        userAvatar.textContent =
            fullName
                .charAt(0)
                .toUpperCase();


        /*
         * Keep localStorage user data
         * synchronized.
         */

        localStorage.setItem(
            "user",
            JSON.stringify(user)
        );

    }

    catch (error) {

        console.error(
            "PROFILE ERROR:",
            error
        );

        /*
         * api.js handles unauthorized
         * requests.
         */

        welcomeName.textContent =
            "User";

        topbarUserName.textContent =
            "User";

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
   MOBILE SIDEBAR
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

loadProfile();