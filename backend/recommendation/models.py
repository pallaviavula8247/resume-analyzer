from django.db import models
from django.conf import settings


class Recommendation(models.Model):
    """
    Stores AI-generated recommendations for a resume.
    """

    PRIORITY_CHOICES = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    CATEGORY_CHOICES = [
        ("Profile", "Profile"),
        ("Skills", "Skills"),
        ("Education", "Education"),
        ("Experience", "Experience"),
        ("Projects", "Projects"),
        ("Certifications", "Certifications"),
        ("ATS", "ATS"),
        ("General", "General"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recommendations",
    )

    resume = models.ForeignKey(
        "parser.Resume",
        on_delete=models.CASCADE,
        related_name="recommendations",
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="Medium",
    )

    message = models.TextField()

    is_resolved = models.BooleanField(
        default=False,
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
        return f"{self.resume.id} - {self.category} - {self.priority}"