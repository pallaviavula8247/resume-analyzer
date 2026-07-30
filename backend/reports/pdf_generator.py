from io import BytesIO

from django.core.files.base import ContentFile

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.units import inch


def generate_report_pdf(report):
    """
    Generate Resume Analysis PDF Report.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # ----------------------------------------------------
    # Title
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>AI Resume Analysis Report</b>",
            styles["Title"],
        )
    )

    story.append(Spacer(1, 0.30 * inch))

    resume = report.resume

    # ----------------------------------------------------
    # Candidate Details
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Candidate Information</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Name:</b> {resume.full_name}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Email:</b> {resume.email}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Phone:</b> {resume.phone}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Location:</b> {resume.location}",
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    # ----------------------------------------------------
    # Scores
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Analysis Scores</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            f"ATS Score : <b>{report.ats_score}%</b>",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"Job Match Score : <b>{report.match_score}%</b>",
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 0.25 * inch))

    # ----------------------------------------------------
    # Skills
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Skills</b>",
            styles["Heading2"],
        )
    )

    for skill in resume.skills:
        story.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.20 * inch))

    # ----------------------------------------------------
    # Missing Skills
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Missing Skills</b>",
            styles["Heading2"],
        )
    )

    for skill in resume.missing_skills:
        story.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.20 * inch))

    # ----------------------------------------------------
    # Education
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Education</b>",
            styles["Heading2"],
        )
    )

    for item in resume.education:
        story.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.20 * inch))

    # ----------------------------------------------------
    # Experience
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Experience</b>",
            styles["Heading2"],
        )
    )

    for item in resume.experience:
        story.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.20 * inch))

    # ----------------------------------------------------
    # Projects
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Projects</b>",
            styles["Heading2"],
        )
    )

    for item in resume.projects:
        story.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.20 * inch))

    # ----------------------------------------------------
    # Certifications
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Certifications</b>",
            styles["Heading2"],
        )
    )

    for item in resume.certifications:
        story.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.20 * inch))

    # ----------------------------------------------------
    # AI Recommendations
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>AI Recommendations</b>",
            styles["Heading2"],
        )
    )

    for recommendation in report.recommendations:
        story.append(
            Paragraph(
                f"• {recommendation}",
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 0.25 * inch))

    # ----------------------------------------------------
    # Footer
    # ----------------------------------------------------

    story.append(
        Paragraph(
            "<b>Generated by Resume Analyzer AI</b>",
            styles["Heading3"],
        )
    )

    story.append(
        Paragraph(
            f"Status : {report.status}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"Generated On : {report.generated_at}",
            styles["BodyText"],
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    filename = f"resume_report_{report.id}.pdf"

    report.pdf_file.save(
        filename,
        ContentFile(pdf),
        save=True,
    )

    return report.pdf_file