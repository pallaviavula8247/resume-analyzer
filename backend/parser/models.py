from django.db import models
from django.conf import settings


class Resume(models.Model):
    """
    Resume Model
    Stores uploaded resume and extracted information.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resumes",
    )

    resume_file = models.FileField(
        upload_to="resumes/",
    )

    extracted_text = models.TextField(
        blank=True,
    )

    full_name = models.CharField(
        max_length=200,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    location = models.CharField(
        max_length=200,
        blank=True,
    )

    linkedin = models.URLField(
        blank=True,
    )

    github = models.URLField(
        blank=True,
    )

    portfolio = models.URLField(
        blank=True,
    )

    skills = models.JSONField(
        default=list,
        blank=True,
    )

    education = models.JSONField(
        default=list,
        blank=True,
    )

    experience = models.JSONField(
        default=list,
        blank=True,
    )

    projects = models.JSONField(
        default=list,
        blank=True,
    )

    certifications = models.JSONField(
        default=list,
        blank=True,
    )

    languages = models.JSONField(
        default=list,
        blank=True,
    )

    ats_score = models.IntegerField(
        default=0,
    )

    missing_skills = models.JSONField(
        default=list,
        blank=True,
    )

    ai_recommendations = models.JSONField(
        default=list,
        blank=True,
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.full_name or self.user.email} Resume"