from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static



def home(request):
    """
    Resume Analyzer Backend API Home
    """

    return JsonResponse(
        {
            "project": "Resume Analyzer API",
            "status": "Running Successfully ✅",
            "version": "1.0.0",
            "developer": "Pallavi Avula",
            "description": "AI Powered Resume Analyzer Backend API",

            "available_endpoints": {

                "home": "/",
                "admin": "/admin/",


                "users": {

                    "register":
                    "/api/users/register/",

                    "login":
                    "/api/users/login/",

                    "refresh_token":
                    "/api/users/token/refresh/",

                    "profile":
                    "/api/users/profile/",
                },


                "parser": {

                    "upload_resume":
                    "/api/parser/upload/",
                },


                "analyzer": {

                    "ats_analysis":
                    "/api/analyzer/analyze/<resume_id>/",

                    "job_matching":
                    "/api/analyzer/match/<resume_id>/",
                },


                "recommendation": {

                    "ai_recommendations":
                    "/api/recommendation/<resume_id>/",
                },


                "dashboard": {

                    "dashboard_api":
                    "/api/dashboard/",
                },


                "reports": {

                    "reports_api":
                    "/api/reports/",

                    "generate_report":
                    "/api/reports/generate/<resume_id>/",

                    "report_history":
                    "/api/reports/",

                    "report_detail":
                    "/api/reports/<report_id>/",

                    "download_saved_report":
                    "/api/reports/<report_id>/download/",

                    "generate_pdf":
                    "/api/reports/<resume_id>/pdf/",
                },
            },
        }
    )



urlpatterns = [

    # ==========================
    # Home API
    # ==========================
    path(
        "",
        home,
        name="home"
    ),


    # ==========================
    # Django Admin
    # ==========================
    path(
        "admin/",
        admin.site.urls
    ),


    # ==========================
    # User APIs
    # ==========================
    path(
        "api/users/",
        include("users.urls")
    ),


    # ==========================
    # Resume Parser APIs
    # ==========================
    path(
        "api/parser/",
        include("parser.urls")
    ),


    # ==========================
    # Analyzer APIs
    # ==========================
    path(
        "api/analyzer/",
        include("analyzer.urls")
    ),


    # ==========================
    # Recommendation APIs
    # ==========================
    path(
        "api/recommendation/",
        include("recommendation.urls")
    ),


    # ==========================
    # Dashboard APIs
    # ==========================
    path(
        "api/dashboard/",
        include("dashboard.urls")
    ),


    # ==========================
    # Reports APIs
    # ==========================
    path(
        "api/reports/",
        include("reports.urls")
    ),

]



# ==============================
# Media Files (Development)
# ==============================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )



# ==============================
# Static Files (Development)
# ==============================

if settings.DEBUG:

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )