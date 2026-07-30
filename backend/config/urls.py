from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    """
    Home API
    """
    return JsonResponse(
        {
            "project": "Resume Analyzer API",
            "status": "Running Successfully ✅",
            "version": "1.0.0",
            "developer": "Pallavi Avula",
            "description": "AI Powered Resume Analyzer Backend API",
            "available_endpoints": {
                "admin": "/admin/",
                "register": "/api/users/register/",
                "login": "/api/users/login/",
                "refresh_token": "/api/users/token/refresh/",
                "profile": "/api/users/profile/",
                "resume_upload": "/api/parser/upload/",
                "job_match": "/api/analyzer/match/<resume_id>/",
                "recommendations": "/api/recommendation/",
                "dashboard": "/api/dashboard/",
                "reports": "/api/reports/",
            },
        }
    )


urlpatterns = [

    # Home
    path("", home),

    # Django Admin
    path("admin/", admin.site.urls),

    # User Authentication
    path("api/users/", include("users.urls")),

    # Resume Parser
    path("api/parser/", include("parser.urls")),

    # Resume Analyzer / Job Matching
    path("api/analyzer/", include("analyzer.urls")),

    # AI Recommendations
    path("api/recommendation/", include("recommendation.urls")),

    # Dashboard
    path("api/dashboard/", include("dashboard.urls")),

    # Reports
    path("api/reports/", include("reports.urls")),

     path(
        "api/users/",
        include("users.urls"),
    ),
]


# ==========================================
# Serve Media Files (Development Only)
# ==========================================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

# ==========================================
# Serve Static Files (Development Only)
# ==========================================

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )