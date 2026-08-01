from django.db import models
from parser.models import Resume


class ATSAnalysis(models.Model):
    """
    Stores ATS analysis results.
    """

    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        related_name="ats_analysis",
    )

    ats_score = models.PositiveIntegerField(default=0)

    keyword_score = models.PositiveIntegerField(default=0)

    skill_score = models.PositiveIntegerField(default=0)

    education_score = models.PositiveIntegerField(default=0)

    experience_score = models.PositiveIntegerField(default=0)

    project_score = models.PositiveIntegerField(default=0)

    certification_score = models.PositiveIntegerField(default=0)

    format_score = models.PositiveIntegerField(default=0)

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

    analyzed_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-analyzed_at"]

    def __str__(self):
        return f"{self.resume.full_name} - ATS {self.ats_score}%"


class JobMatch(models.Model):
    """
    Stores job matching results.
    """

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="job_matches",
    )

    job_title = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    job_description = models.TextField()

    match_score = models.PositiveIntegerField(
        default=0,
    )

    match_level = models.CharField(
        max_length=30,
        default="",
        blank=True,
    )

    matched_skills = models.JSONField(
        default=list,
        blank=True,
    )

    missing_skills = models.JSONField(
        default=list,
        blank=True,
    )

    extra_skills = models.JSONField(
        default=list,
        blank=True,
    )

    recommendations = models.JSONField(
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

    def __str__(self):
        return f"{self.resume.full_name} - {self.match_score}% Match"