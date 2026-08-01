from django.db import models
from parser.models import Resume


class Recommendation(models.Model):
    """
    Stores AI-generated recommendations for a resume.
    """

    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        related_name="recommendation",
    )

    recommended_roles = models.JSONField(
        default=list,
        blank=True,
    )

    recommended_skills = models.JSONField(
        default=list,
        blank=True,
    )

    recommended_courses = models.JSONField(
        default=list,
        blank=True,
    )

    recommended_projects = models.JSONField(
        default=list,
        blank=True,
    )

    learning_roadmap = models.JSONField(
        default=list,
        blank=True,
    )

    resume_tips = models.JSONField(
        default=list,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Recommendation"
        verbose_name_plural = "Recommendations"

    def __str__(self):
        return f"Recommendations - {self.resume.full_name}"