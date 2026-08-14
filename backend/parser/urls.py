"""
parser/urls.py

URL Configuration for Resume Parser
"""

from django.urls import path

from .views import (
    ResumeUploadView,
    ResumeListView,
)

app_name = "parser"

urlpatterns = [

    # =====================================
    # Upload Resume
    # POST /api/parser/upload/
    # =====================================
    path(
        "upload/",
        ResumeUploadView.as_view(),
        name="upload-resume",
    ),

    # =====================================
    # List Uploaded Resumes
    # GET /api/parser/list/
    # =====================================
    path(
        "list/",
        ResumeListView.as_view(),
        name="resume-list",
    ),

]