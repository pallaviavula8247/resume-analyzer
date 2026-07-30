from django.db import models

from parser.models import Resume


class JobMatch(models.Model):

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="job_matches",
    )

    job_title = models.CharField(
        max_length=200,
        blank=True,
    )

    job_description = models.TextField()

    match_score = models.FloatField(
        default=0,
    )

    matched_skills = models.JSONField(
        default=list,
    )

    missing_skills = models.JSONField(
        default=list,
    )

    recommendations = models.JSONField(
        default=list,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.resume.full_name} - {self.match_score}%"