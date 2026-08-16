/* =========================================================
   RESUME AI - LOGIN
   ========================================================= */

const loginForm = document.getElementById("loginForm");
const loginButton = document.getElementById("loginButton");
const loginMessage = document.getElementById("loginMessage");

const togglePassword =
    document.getElementById("togglePassword");

const passwordInput =
    document.getElementById("password");


/* =========================================================
   SHOW MESSAGE
   ========================================================= */

function showLoginMessage(message, type = "error") {

    loginMessage.textContent = message;

    loginMessage.className =
        `auth-message show ${type}`;
}


/* =========================================================
   PASSWORD TOGGLE
   ========================================================= */

togglePassword.addEventListener(
    "click",
    () => {

        const isPassword =
            passwordInput.type === "password";

        passwordInput.type =
            isPassword
                ? "text"
                : "password";

        togglePassword.textContent =
            isPassword
                ? "Hide"
                : "Show";
    }
);


/* =========================================================
   LOGIN
   ========================================================= */

loginForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        loginMessage.className =
            "auth-message";

        const email =
            document.getElementById("email")
                .value
                .trim();

        const password =
            passwordInput.value;


        if (!email || !password) {

            showLoginMessage(
                "Please enter your email and password."
            );

            return;
        }


        loginButton.disabled = true;

        loginButton.classList.add("loading");

        loginButton.textContent =
            "Signing in...";


        try {

            const data = await apiPost(
                "/users/login/",
                {
                    email,
                    password
                }
            );


            if (!data.success) {

                throw new Error(
                    data.message ||
                    "Login failed."
                );
            }


            /*
             * Save JWT tokens.
             */

            saveTokens(
                data.access,
                data.refresh
            );


            /*
             * Save user information for quick
             * frontend access.
             */

            if (data.user) {

                localStorage.setItem(
                    "user",
                    JSON.stringify(data.user)
                );
            }


            showLoginMessage(
                "Login successful. Redirecting...",
                "success"
            );


            setTimeout(
                () => {

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
                error.message ||
                "Unable to login. Please try again."
            );

        }

        finally {

            loginButton.disabled = false;

            loginButton.classList.remove(
                "loading"
            );

            loginButton.textContent =
                "Sign In";
        }

    }
);