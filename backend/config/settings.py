from pathlib import Path
from datetime import timedelta


# =============================================================
# BASE DIRECTORY
# =============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================
# SECURITY
# =============================================================

SECRET_KEY = "django-insecure-change-this-in-production"

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# =============================================================
# APPLICATIONS
# =============================================================

INSTALLED_APPS = [

    # ---------------------------------------------------------
    # Django
    # ---------------------------------------------------------

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # ---------------------------------------------------------
    # Third-party
    # ---------------------------------------------------------

    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",

    # ---------------------------------------------------------
    # Project apps
    # ---------------------------------------------------------

    "users",
    "parser",
    "analyzer",
    "recommendation",
    "reports",
    "dashboard",
]


# =============================================================
# CUSTOM USER MODEL
# =============================================================
#
# IMPORTANT:
# Your project has a custom User model:
#
# users.models.User
#
# Django must use this instead of auth.User.
#
# =============================================================

AUTH_USER_MODEL = "users.User"


# =============================================================
# MIDDLEWARE
# =============================================================

MIDDLEWARE = [

    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =============================================================
# URL CONFIGURATION
# =============================================================

ROOT_URLCONF = "config.urls"


# =============================================================
# TEMPLATES
# =============================================================

TEMPLATES = [

    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


# =============================================================
# WSGI
# =============================================================

WSGI_APPLICATION = "config.wsgi.application"


# =============================================================
# DATABASE
# =============================================================

DATABASES = {

    "default": {

        "ENGINE":
            "django.db.backends.sqlite3",

        "NAME":
            BASE_DIR / "db.sqlite3",

    }

}


# =============================================================
# PASSWORD VALIDATION
# =============================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]


# =============================================================
# INTERNATIONALIZATION
# =============================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =============================================================
# STATIC FILES
# =============================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# =============================================================
# MEDIA FILES
# =============================================================
#
# Uploaded resumes:
#
# media/resumes/
#
# Generated reports:
#
# media/reports/
#
# Browser URLs:
#
# http://127.0.0.1:8000/media/resumes/...
#
# http://127.0.0.1:8000/media/reports/...
#
# =============================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =============================================================
# DEFAULT PRIMARY KEY
# =============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =============================================================
# DJANGO REST FRAMEWORK
# =============================================================

REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": [

        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ],

    "DEFAULT_PERMISSION_CLASSES": [

        "rest_framework.permissions.IsAuthenticated",

    ],

}


# =============================================================
# CORS
# =============================================================
#
# Plain HTML / CSS / JavaScript frontend
#
# =============================================================

CORS_ALLOW_ALL_ORIGINS = True


# =============================================================
# CSRF TRUSTED ORIGINS
# =============================================================

CSRF_TRUSTED_ORIGINS = [

    "http://127.0.0.1:8000",

    "http://localhost:8000",

]


# =============================================================
# JWT SETTINGS
# =============================================================

SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME":
        timedelta(minutes=60),

    "REFRESH_TOKEN_LIFETIME":
        timedelta(days=7),

    "ROTATE_REFRESH_TOKENS":
        True,

    "BLACKLIST_AFTER_ROTATION":
        False,

    "AUTH_HEADER_TYPES":
        ("Bearer",),

}

