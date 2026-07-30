from django.urls import path

from .views import JobMatchView

urlpatterns = [
    path(
        "match/<int:resume_id>/",
        JobMatchView.as_view(),
        name="job_match",
    ),
]