from django.db import models
from parser.models import Resume


class ATSAnalysis(models.Model):
    """
    Stores ATS analysis results for a parsed resume.
    """

    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        related_name="ats_analysis",
    )

    # Overall ATS Score
    ats_score = models.PositiveIntegerField(default=0)

    # Individual Scores
    keyword_score = models.PositiveIntegerField(default=0)
    skill_score = models.PositiveIntegerField(default=0)
    education_score = models.PositiveIntegerField(default=0)
    experience_score = models.PositiveIntegerField(default=0)
    project_score = models.PositiveIntegerField(default=0)
    certification_score = models.PositiveIntegerField(default=0)
    format_score = models.PositiveIntegerField(default=0)

    # Analysis Results
    strengths = models.JSONField(
        default=list,
        blank=True,
    )

    weaknesses = models.JSONField(
        default=list,
        blank=True,
    )

    missing_skills = models.JSONField(
        default=list,
        blank=True,
    )

    recommendations = models.JSONField(
        default=list,
        blank=True,
    )

    # Timestamps
    analyzed_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-analyzed_at"]
        verbose_name = "ATS Analysis"
        verbose_name_plural = "ATS Analyses"

    def __str__(self):
        name = self.resume.full_name or self.resume.email or "Unknown User"
        return f"{name} - ATS Score: {self.ats_score}%"