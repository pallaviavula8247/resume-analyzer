/* =========================================================
   RESUME AI - REGISTER
   ========================================================= */

const registerForm =
    document.getElementById("registerForm");

const registerButton =
    document.getElementById("registerButton");

const registerMessage =
    document.getElementById("registerMessage");

const togglePassword =
    document.getElementById("togglePassword");

const passwordInput =
    document.getElementById("password");


/* =========================================================
   MESSAGE
   ========================================================= */

function showRegisterMessage(
    message,
    type = "error"
) {

    registerMessage.textContent =
        message;

    registerMessage.className =
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
   REGISTER
   ========================================================= */

registerForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        registerMessage.className =
            "auth-message";


        const fullName =
            document.getElementById("fullName")
                .value
                .trim();

        const email =
            document.getElementById("email")
                .value
                .trim();

        const phone =
            document.getElementById("phone")
                .value
                .trim();

        const password =
            passwordInput.value;

        const confirmPassword =
            document.getElementById(
                "confirmPassword"
            ).value;


        /* =================================================
           CLIENT VALIDATION
           ================================================= */

        if (!fullName) {

            showRegisterMessage(
                "Please enter your full name."
            );

            return;
        }


        if (!email) {

            showRegisterMessage(
                "Please enter your email address."
            );

            return;
        }


        if (password.length < 6) {

            showRegisterMessage(
                "Password must contain at least 6 characters."
            );

            return;
        }


        if (password !== confirmPassword) {

            showRegisterMessage(
                "Passwords do not match."
            );

            return;
        }


        /* =================================================
           DISABLE BUTTON
           ================================================= */

        registerButton.disabled = true;

        registerButton.classList.add(
            "loading"
        );

        registerButton.textContent =
            "Creating account...";


        try {

            const data = await apiPost(
                "/users/register/",
                {
                    full_name: fullName,
                    email: email,
                    phone: phone,
                    password: password
                }
            );


            if (!data.success) {

                throw new Error(
                    data.message ||
                    "Registration failed."
                );
            }


            showRegisterMessage(
                "Registration successful. Redirecting to login...",
                "success"
            );


            registerForm.reset();


            setTimeout(
                () => {

                    window.location.href =
                        "login.html";

                },
                1000
            );

        }

        catch (error) {

            console.error(
                "REGISTER ERROR:",
                error
            );


            showRegisterMessage(
                error.message ||
                "Unable to create account."
            );

        }

        finally {

            registerButton.disabled =
                false;

            registerButton.classList.remove(
                "loading"
            );

            registerButton.textContent =
                "Create Account";
        }

    }
);