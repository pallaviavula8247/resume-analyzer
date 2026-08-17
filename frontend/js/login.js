/* =========================================================
   RESUME AI - LOGIN
   ========================================================= */

console.log("LOGIN.JS LOADED");


/* =========================================================
   ELEMENTS
   ========================================================= */

const loginForm =
    document.getElementById("loginForm");

const loginButton =
    document.getElementById("loginButton");

const loginMessage =
    document.getElementById("loginMessage");

const emailInput =
    document.getElementById("email");

const passwordInput =
    document.getElementById("password");


/* =========================================================
   DEBUG
   ========================================================= */

console.log("LOGIN FORM:", loginForm);
console.log("EMAIL INPUT:", emailInput);
console.log("PASSWORD INPUT:", passwordInput);
console.log("LOGIN BUTTON:", loginButton);
console.log("LOGIN MESSAGE:", loginMessage);


/* =========================================================
   CHECK REQUIRED ELEMENTS
   ========================================================= */

if (!loginForm) {

    console.error(
        "LOGIN FORM NOT FOUND: #loginForm"
    );

}


/* =========================================================
   SHOW MESSAGE
   ========================================================= */

function showLoginMessage(
    message,
    type = "error"
) {

    if (!loginMessage) {

        console.error(
            "LOGIN MESSAGE ELEMENT NOT FOUND"
        );

        return;

    }


    loginMessage.textContent =
        message;


    if (!message) {

        loginMessage.style.display =
            "none";

        loginMessage.className =
            "auth-message";

        return;

    }


    loginMessage.style.display =
        "block";


    loginMessage.className =
        `auth-message ${type}`;

}


/* =========================================================
   LOGIN FORM
   ========================================================= */

if (loginForm) {

    loginForm.addEventListener(
        "submit",
        async function (event) {

            event.preventDefault();


            console.log(
                "LOGIN FORM SUBMITTED"
            );


            /* =================================================
               GET VALUES
               ================================================= */

            const email =
                emailInput
                    ? emailInput.value.trim()
                    : "";

            const password =
                passwordInput
                    ? passwordInput.value
                    : "";


            console.log(
                "LOGIN EMAIL:",
                email
            );


            /* =================================================
               VALIDATION
               ================================================= */

            if (!email) {

                showLoginMessage(
                    "Please enter your email."
                );

                if (emailInput) {
                    emailInput.focus();
                }

                return;

            }


            if (!password) {

                showLoginMessage(
                    "Please enter your password."
                );

                if (passwordInput) {
                    passwordInput.focus();
                }

                return;

            }


            /* =================================================
               BUTTON LOADING
               ================================================= */

            if (loginButton) {

                loginButton.disabled =
                    true;

                loginButton.textContent =
                    "Signing in...";

            }


            showLoginMessage(
                "",
                ""
            );


            try {

                console.log(
                    "LOGIN REQUEST STARTED"
                );


                /* =================================================
                   API
                   
                   POST /api/users/login/
                   ================================================= */

                const response =
                    await apiPost(
                        "/users/login/",
                        {
                            email: email,
                            password: password
                        }
                    );


                console.log(
                    "LOGIN RESPONSE:",
                    response
                );


                /* =================================================
                   GET TOKENS
                   ================================================= */

                const access =
                    response?.access ||
                    response?.access_token;


                const refresh =
                    response?.refresh ||
                    response?.refresh_token;


                /* =================================================
                   CHECK ACCESS TOKEN
                   ================================================= */

                if (!access) {

                    console.error(
                        "ACCESS TOKEN NOT FOUND:",
                        response
                    );

                    throw new Error(
                        "Login failed. Access token was not returned."
                    );

                }


                /* =================================================
                   SAVE TOKENS
                   ================================================= */

                saveTokens(
                    access,
                    refresh || null
                );


                console.log(
                    "ACCESS TOKEN SAVED"
                );


                console.log(
                    "REFRESH TOKEN SAVED:",
                    Boolean(refresh)
                );


                /* =================================================
                   SUCCESS
                   ================================================= */

                showLoginMessage(
                    "Login successful. Redirecting...",
                    "success"
                );


                /* =================================================
                   REDIRECT TO DASHBOARD
                   
                   login.html
                   dashboard.html

                   Both are inside pages/
                   ================================================= */

                setTimeout(
                    function () {

                        window.location.href =
                            "dashboard.html";

                    },
                    500
                );


            }

            catch (error) {

                console.error(
                    "LOGIN ERROR:",
                    error
                );


                showLoginMessage(
                    error?.message ||
                    "Invalid email or password."
                );

            }

            finally {

                if (loginButton) {

                    loginButton.disabled =
                        false;

                    loginButton.textContent =
                        "Sign In";

                }

            }

        }
    );

}


/* =========================================================
   ENTER KEY SUPPORT
   ========================================================= */

if (passwordInput) {

    passwordInput.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Enter"
            ) {

                if (loginForm) {

                    loginForm.requestSubmit();

                }

            }

        }
    );

}


/* =========================================================
   PAGE LOADED
   ========================================================= */

console.log(
    "LOGIN PAGE READY"
);