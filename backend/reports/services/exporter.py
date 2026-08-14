"""
reports/services/exporter.py

Export the complete Resume Analyzer report as a PDF.
"""

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)

from reports.services.report_builder import build_report


def _safe_text(value):
    """
    Convert values into safe text for ReportLab.
    """
    if value is None:
        return ""

    if isinstance(value, list):
        return ", ".join(str(item) for item in value)

    return str(value)


def _add_bullets(story, items, style):
    """
    Add a list of bullet points.
    """

    if not items:
        story.append(
            Paragraph("No information available.", style)
        )
        return

    for item in items:
        story.append(
            Paragraph(
                f"• {_safe_text(item)}",
                style,
            )
        )
        story.append(Spacer(1, 2 * mm))


def export_report_pdf(resume_id):
    """
    Generate a PDF report for the given resume.

    Returns:
        BytesIO object containing the PDF.
    """

    report = build_report(resume_id)

    if not report:
        return None

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
        title="AI Resume Analyzer Report",
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=8 * mm,
    )

    heading_style = ParagraphStyle(
        "ReportHeading",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=6 * mm,
        spaceAfter=4 * mm,
    )

    subheading_style = ParagraphStyle(
        "ReportSubHeading",
        parent=styles["Heading3"],
        fontSize=11,
        spaceBefore=4 * mm,
        spaceAfter=2 * mm,
    )

    body_style = ParagraphStyle(
        "ReportBody",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13,
        spaceAfter=2 * mm,
    )

    small_style = ParagraphStyle(
        "ReportSmall",
        parent=styles["BodyText"],
        fontSize=8,
        leading=11,
    )

    story = []

    # ==================================================
    # TITLE
    # ==================================================

    story.append(
        Paragraph(
            report["report_info"]["title"],
            title_style,
        )
    )

    story.append(
        Paragraph(
            f"Generated: {report['report_info']['generated_at']}",
            small_style,
        )
    )

    story.append(
        Paragraph(
            f"Version: {report['report_info']['version']}",
            small_style,
        )
    )

    story.append(Spacer(1, 8 * mm))

    # ==================================================
    # CANDIDATE
    # ==================================================

    story.append(
        Paragraph(
            "1. Candidate Information",
            heading_style,
        )
    )

    candidate = report["candidate"]

    candidate_data = [
        ["Resume ID", _safe_text(candidate["resume_id"])],
        ["Name", _safe_text(candidate["name"])],
        ["Email", _safe_text(candidate["email"])],
        ["Phone", _safe_text(candidate["phone"])],
        ["Location", _safe_text(candidate["location"])],
        ["LinkedIn", _safe_text(candidate["linkedin"])],
        ["GitHub", _safe_text(candidate["github"])],
        ["Portfolio", _safe_text(candidate["portfolio"])],
    ]

    table = Table(
        candidate_data,
        colWidths=[40 * mm, 135 * mm],
    )

    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("PADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )

    story.append(table)

    # ==================================================
    # SUMMARY
    # ==================================================

    story.append(
        Paragraph(
            "2. Resume Analysis Summary",
            heading_style,
        )
    )

    summary = report["summary"]

    summary_data = [
        ["ATS Score", _safe_text(summary["ats_score"])],
        ["ATS Category", _safe_text(summary["ats_category"])],
        ["Job Matches", _safe_text(summary["job_matches"])],
        ["Missing Skills", _safe_text(summary["missing_skills"])],
    ]

    summary_table = Table(
        summary_data,
        colWidths=[60 * mm, 115 * mm],
    )

    summary_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("PADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )

    story.append(summary_table)

    # ==================================================
    # ATS ANALYSIS
    # ==================================================

    story.append(
        Paragraph(
            "3. ATS Analysis",
            heading_style,
        )
    )

    ats = report["ats_analysis"]

    if ats:

        ats_scores = [
            ["Metric", "Score"],
            ["ATS Score", _safe_text(ats["ats_score"])],
            ["Keyword Score", _safe_text(ats["keyword_score"])],
            ["Skill Score", _safe_text(ats["skill_score"])],
            ["Education Score", _safe_text(ats["education_score"])],
            ["Experience Score", _safe_text(ats["experience_score"])],
            ["Project Score", _safe_text(ats["project_score"])],
            [
                "Certification Score",
                _safe_text(ats["certification_score"]),
            ],
            ["Format Score", _safe_text(ats["format_score"])],
        ]

        ats_table = Table(
            ats_scores,
            colWidths=[100 * mm, 75 * mm],
        )

        ats_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("PADDING", (0, 0), (-1, -1), 5),
                ]
            )
        )

        story.append(ats_table)

        story.append(
            Paragraph("Strengths", subheading_style)
        )

        _add_bullets(
            story,
            ats["strengths"],
            body_style,
        )

        story.append(
            Paragraph("Weaknesses", subheading_style)
        )

        _add_bullets(
            story,
            ats["weaknesses"],
            body_style,
        )

        story.append(
            Paragraph("Missing Skills", subheading_style)
        )

        _add_bullets(
            story,
            ats["missing_skills"],
            body_style,
        )

        story.append(
            Paragraph("ATS Recommendations", subheading_style)
        )

        _add_bullets(
            story,
            ats["recommendations"],
            body_style,
        )

    else:

        story.append(
            Paragraph(
                "ATS analysis has not been generated yet.",
                body_style,
            )
        )

    # ==================================================
    # JOB MATCHES
    # ==================================================

    story.append(PageBreak())

    story.append(
        Paragraph(
            "4. Job Match Analysis",
            heading_style,
        )
    )

    job_matches = report["job_matches"]

    if job_matches:

        for index, match in enumerate(job_matches, start=1):

            story.append(
                Paragraph(
                    f"{index}. {_safe_text(match['job_title'])}",
                    subheading_style,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Match Score:</b> "
                    f"{_safe_text(match['match_score'])}",
                    body_style,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Match Level:</b> "
                    f"{_safe_text(match['match_level'])}",
                    body_style,
                )
            )

            story.append(
                Paragraph(
                    "<b>Matched Skills:</b> "
                    + _safe_text(match["matched_skills"]),
                    body_style,
                )
            )

            story.append(
                Paragraph(
                    "<b>Missing Skills:</b> "
                    + _safe_text(match["missing_skills"]),
                    body_style,
                )
            )

            story.append(
                Paragraph(
                    "<b>Extra Skills:</b> "
                    + _safe_text(match["extra_skills"]),
                    body_style,
                )
            )

            _add_bullets(
                story,
                match["recommendations"],
                body_style,
            )

            story.append(Spacer(1, 4 * mm))

    else:

        story.append(
            Paragraph(
                "No job matches available.",
                body_style,
            )
        )

    # ==================================================
    # PHASE 7 RECOMMENDATIONS
    # ==================================================

    story.append(PageBreak())

    story.append(
        Paragraph(
            "5. AI Career Recommendations",
            heading_style,
        )
    )

    recommendations = report["recommendations"]

    # --------------------------------------------------
    # Recommended Roles
    # --------------------------------------------------

    story.append(
        Paragraph(
            "Recommended Career Roles",
            subheading_style,
        )
    )

    _add_bullets(
        story,
        recommendations["recommended_roles"],
        body_style,
    )

    # --------------------------------------------------
    # Recommended Skills
    # --------------------------------------------------

    story.append(
        Paragraph(
            "Recommended Skills",
            subheading_style,
        )
    )

    _add_bullets(
        story,
        recommendations["recommended_skills"],
        body_style,
    )

    # --------------------------------------------------
    # Recommended Courses
    # --------------------------------------------------

    story.append(
        Paragraph(
            "Recommended Courses",
            subheading_style,
        )
    )

    courses = recommendations["recommended_courses"]

    if courses:

        for course in courses:

            if isinstance(course, dict):

                title = course.get(
                    "title",
                    course.get("name", ""),
                )

                description = course.get(
                    "description",
                    "",
                )

                story.append(
                    Paragraph(
                        f"<b>{_safe_text(title)}</b>",
                        body_style,
                    )
                )

                if description:
                    story.append(
                        Paragraph(
                            _safe_text(description),
                            small_style,
                        )
                    )

            else:

                story.append(
                    Paragraph(
                        f"• {_safe_text(course)}",
                        body_style,
                    )
                )

    else:

        story.append(
            Paragraph(
                "No course recommendations available yet.",
                body_style,
            )
        )

    # --------------------------------------------------
    # Recommended Projects
    # --------------------------------------------------

    story.append(
        Paragraph(
            "Recommended Projects",
            subheading_style,
        )
    )

    projects = recommendations["recommended_projects"]

    if projects:

        for project in projects:

            if isinstance(project, dict):

                title = project.get(
                    "title",
                    "Project",
                )

                difficulty = project.get(
                    "difficulty",
                    "",
                )

                technologies = project.get(
                    "technologies",
                    [],
                )

                story.append(
                    Paragraph(
                        f"<b>{_safe_text(title)}</b>",
                        body_style,
                    )
                )

                story.append(
                    Paragraph(
                        f"Difficulty: "
                        f"{_safe_text(difficulty)}",
                        small_style,
                    )
                )

                story.append(
                    Paragraph(
                        "Technologies: "
                        + _safe_text(technologies),
                        small_style,
                    )
                )

                story.append(
                    Spacer(1, 2 * mm)
                )

    else:

        story.append(
            Paragraph(
                "No project recommendations available.",
                body_style,
            )
        )

    # --------------------------------------------------
    # Learning Roadmap
    # --------------------------------------------------

    story.append(
        Paragraph(
            "Learning Roadmap",
            subheading_style,
        )
    )

    roadmap = recommendations["learning_roadmap"]

    if roadmap:

        for career, steps in roadmap.items():

            story.append(
                Paragraph(
                    f"<b>{_safe_text(career)}</b>",
                    body_style,
                )
            )

            _add_bullets(
                story,
                steps,
                small_style,
            )

    else:

        story.append(
            Paragraph(
                "No learning roadmap available.",
                body_style,
            )
        )

    # --------------------------------------------------
    # Resume Tips
    # --------------------------------------------------

    story.append(
        Paragraph(
            "Resume Improvement Tips",
            subheading_style,
        )
    )

    _add_bullets(
        story,
        recommendations["resume_tips"],
        body_style,
    )

    # ==================================================
    # BUILD PDF
    # ==================================================

    document.build(story)

    buffer.seek(0)

    return buffer