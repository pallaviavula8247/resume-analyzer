from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Resume AI API is running successfully.",
        "status": "ok"
    })


urlpatterns = [

    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path(
        "api/users/",
        include("users.urls")
    ),

    path(
        "api/parser/",
        include("parser.urls")
    ),

    path(
        "api/analyzer/",
        include("analyzer.urls")
    ),

    path(
        "api/recommendation/",
        include("recommendation.urls")
    ),

    path(
        "api/reports/",
        include("reports.urls")
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )