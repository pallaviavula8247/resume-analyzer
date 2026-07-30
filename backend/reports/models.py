from django.db import models
from parser.models import Resume


class Report(models.Model):
    """
    Stores generated AI Resume Analysis Reports.
    """

    REPORT_STATUS = [
        ("Pending", "Pending"),
        ("Generated", "Generated"),
        ("Downloaded", "Downloaded"),
        ("Failed", "Failed"),
    ]

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="reports",
    )

    report_title = models.CharField(
        max_length=200,
    )

    report_version = models.CharField(
        max_length=20,
        default="1.0",
    )

    # Analysis Results
    ats_score = models.PositiveIntegerField(
        default=0,
    )

    match_score = models.PositiveIntegerField(
        default=0,
    )

    parsed_data = models.JSONField(
        default=dict,
        blank=True,
    )

    recommendations = models.JSONField(
        default=list,
        blank=True,
    )

    pdf_file = models.FileField(
        upload_to="reports/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=REPORT_STATUS,
        default="Pending",
    )

    generated_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-generated_at"]

    def __str__(self):
        return f"Report #{self.id} - {self.resume.user.email}"