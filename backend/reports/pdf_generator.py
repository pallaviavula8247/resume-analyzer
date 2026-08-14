"""
reports/services/pdf_generator.py

Generate PDF reports for the Resume Analyzer.
"""

import os

from django.conf import settings

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)

from .report_builder import build_report


# ============================================================
# Helper Functions
# ============================================================

def safe_text(value, default="Not Available"):
    """
    Convert values safely into printable text.
    """

    if value is None:
        return default

    if isinstance(value, list):
        if not value:
            return default

        return ", ".join(str(item) for item in value)

    if isinstance(value, dict):
        if not value:
            return default

        return ", ".join(
            f"{key}: {value}"
            for key, value in value.items()
        )

    text = str(value).strip()

    return text if text else default


def add_section_title(story, title, styles):
    """
    Add a section heading to the PDF.
    """

    story.append(
        Paragraph(
            title,
            styles["SectionTitle"]
        )
    )

    story.append(
        Spacer(1, 8)
    )


def add_bullet_list(story, items, styles):
    """
    Add bullet points to the PDF.
    """

    if not items:
        story.append(
            Paragraph(
                "Not Available",
                styles["Body"]
            )
        )
        return

    for item in items:

        if isinstance(item, dict):
            text = " | ".join(
                f"{key}: {value}"
                for key, value in item.items()
            )
        else:
            text = str(item)

        story.append(
            Paragraph(
                f"• {text}",
                styles["Body"]
            )
        )

        story.append(
            Spacer(1, 4)
        )


# ============================================================
# Main PDF Generator
# ============================================================

def generate_pdf_report(resume_id):
    """
    Generate a PDF report for a resume.

    Parameters
    ----------
    resume_id : int
        Resume primary key.

    Returns
    -------
    str or None
        Absolute path of generated PDF.
    """

    # --------------------------------------------------------
    # Build report data
    # --------------------------------------------------------

    report = build_report(resume_id)

    if not report:
        return None

    # --------------------------------------------------------
    # Create report directory
    # --------------------------------------------------------

    report_directory = os.path.join(
        settings.MEDIA_ROOT,
        "reports",
    )

    os.makedirs(
        report_directory,
        exist_ok=True,
    )

    # --------------------------------------------------------
    # PDF file path
    # --------------------------------------------------------

    file_name = f"resume_report_{resume_id}.pdf"

    file_path = os.path.join(
        report_directory,
        file_name,
    )

    # --------------------------------------------------------
    # PDF document
    # --------------------------------------------------------

    document = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
        title="AI Resume Analyzer Report",
        author="Resume Analyzer",
    )

    # --------------------------------------------------------
    # Styles
    # --------------------------------------------------------

    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            fontSize=20,
            leading=24,
            spaceAfter=12,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            parent=styles["Heading2"],
            fontSize=14,
            leading=18,
            spaceBefore=12,
            spaceAfter=8,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SubTitle",
            parent=styles["Heading3"],
            fontSize=11,
            leading=14,
            spaceBefore=8,
            spaceAfter=5,
        )
    )

    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["BodyText"],
            fontSize=9,
            leading=13,
            spaceAfter=4,
        )
    )

    styles.add(
        ParagraphStyle(
            name="Small",
            parent=styles["BodyText"],
            fontSize=8,
            leading=11,
        )
    )

    # --------------------------------------------------------
    # Story
    # --------------------------------------------------------

    story = []

    # ========================================================
    # TITLE
    # ========================================================

    story.append(
        Paragraph(
            "AI Resume Analyzer Report",
            styles["ReportTitle"],
        )
    )

    story.append(
        Paragraph(
            safe_text(
                report.get("report_info", {}).get(
                    "generated_at"
                )
            ),
            styles["Small"],
        )
    )

    story.append(
        Spacer(1, 15)
    )

    # ========================================================
    # CANDIDATE INFORMATION
    # ========================================================

    add_section_title(
        story,
        "1. Candidate Information",
        styles,
    )

    candidate = report.get(
        "candidate",
        {}
    )

    candidate_data = [
        [
            "Resume ID",
            safe_text(candidate.get("resume_id")),
        ],
        [
            "Name",
            safe_text(candidate.get("name")),
        ],
        [
            "Email",
            safe_text(candidate.get("email")),
        ],
        [
            "Phone",
            safe_text(candidate.get("phone")),
        ],
        [
            "Resume File",
            safe_text(candidate.get("resume_file")),
        ],
    ]

    table = Table(
        candidate_data,
        colWidths=[1.5 * inch, 4.8 * inch],
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey,
                ),
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.lightgrey,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, -1),
                    "Helvetica",
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
            ]
        )
    )

    story.append(table)

    # ========================================================
    # SUMMARY
    # ========================================================

    add_section_title(
        story,
        "2. Resume Summary",
        styles,
    )

    summary = report.get(
        "summary",
        {}
    )

    summary_data = [
        [
            "ATS Score",
            safe_text(
                summary.get("ats_score"),
                "0",
            ),
        ],
        [
            "ATS Category",
            safe_text(
                summary.get("ats_category")
            ),
        ],
        [
            "Job Matches",
            safe_text(
                summary.get("job_matches"),
                "0",
            ),
        ],
        [
            "Missing Skills",
            safe_text(
                summary.get("missing_skills"),
                "0",
            ),
        ],
    ]

    summary_table = Table(
        summary_data,
        colWidths=[2.5 * inch, 3.8 * inch],
    )

    summary_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey,
                ),
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.lightgrey,
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
            ]
        )
    )

    story.append(summary_table)

    # ========================================================
    # ATS ANALYSIS
    # ========================================================

    add_section_title(
        story,
        "3. ATS Analysis",
        styles,
    )

    ats = report.get(
        "ats_analysis"
    )

    if ats:

        ats_data = [
            [
                "ATS Score",
                safe_text(ats.get("ats_score"), "0"),
            ],
            [
                "Keyword Score",
                safe_text(ats.get("keyword_score"), "0"),
            ],
            [
                "Skill Score",
                safe_text(ats.get("skill_score"), "0"),
            ],
            [
                "Education Score",
                safe_text(ats.get("education_score"), "0"),
            ],
            [
                "Experience Score",
                safe_text(ats.get("experience_score"), "0"),
            ],
            [
                "Project Score",
                safe_text(ats.get("project_score"), "0"),
            ],
            [
                "Certification Score",
                safe_text(
                    ats.get("certification_score"),
                    "0",
                ),
            ],
            [
                "Format Score",
                safe_text(
                    ats.get("format_score"),
                    "0",
                ),
            ],
        ]

        ats_table = Table(
            ats_data,
            colWidths=[3 * inch, 3.3 * inch],
        )

        ats_table.setStyle(
            TableStyle(
                [
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey,
                    ),
                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, -1),
                        colors.lightgrey,
                    ),
                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        6,
                    ),
                ]
            )
        )

        story.append(ats_table)

        story.append(
            Spacer(1, 10)
        )

        story.append(
            Paragraph(
                "<b>Strengths</b>",
                styles["SubTitle"],
            )
        )

        add_bullet_list(
            story,
            ats.get("strengths", []),
            styles,
        )

        story.append(
            Paragraph(
                "<b>Weaknesses</b>",
                styles["SubTitle"],
            )
        )

        add_bullet_list(
            story,
            ats.get("weaknesses", []),
            styles,
        )

        story.append(
            Paragraph(
                "<b>Missing Skills</b>",
                styles["SubTitle"],
            )
        )

        add_bullet_list(
            story,
            ats.get("missing_skills", []),
            styles,
        )

        story.append(
            Paragraph(
                "<b>Recommendations</b>",
                styles["SubTitle"],
            )
        )

        add_bullet_list(
            story,
            ats.get("recommendations", []),
            styles,
        )

    else:

        story.append(
            Paragraph(
                "ATS analysis has not been generated yet.",
                styles["Body"],
            )
        )

    # ========================================================
    # JOB MATCHES
    # ========================================================

    story.append(
        PageBreak()
    )

    add_section_title(
        story,
        "4. Job Matches",
        styles,
    )

    job_matches = report.get(
        "job_matches",
        []
    )

    if job_matches:

        for index, job in enumerate(
            job_matches,
            start=1,
        ):

            story.append(
                Paragraph(
                    f"{index}. {safe_text(job.get('job_title'))}",
                    styles["SubTitle"],
                )
            )

            story.append(
                Paragraph(
                    f"<b>Match Score:</b> "
                    f"{safe_text(job.get('match_score'), '0')}%",
                    styles["Body"],
                )
            )

            story.append(
                Paragraph(
                    f"<b>Match Level:</b> "
                    f"{safe_text(job.get('match_level'))}",
                    styles["Body"],
                )
            )

            story.append(
                Paragraph(
                    "<b>Matched Skills</b>",
                    styles["Body"],
                )
            )

            add_bullet_list(
                story,
                job.get("matched_skills", []),
                styles,
            )

            story.append(
                Paragraph(
                    "<b>Missing Skills</b>",
                    styles["Body"],
                )
            )

            add_bullet_list(
                story,
                job.get("missing_skills", []),
                styles,
            )

            story.append(
                Paragraph(
                    "<b>Recommendations</b>",
                    styles["Body"],
                )
            )

            add_bullet_list(
                story,
                job.get("recommendations", []),
                styles,
            )

            story.append(
                Spacer(1, 10)
            )

    else:

        story.append(
            Paragraph(
                "No job matches available.",
                styles["Body"],
            )
        )

    # ========================================================
    # AI RECOMMENDATIONS
    # ========================================================

    add_section_title(
        story,
        "5. AI Recommendations",
        styles,
    )

    recommendations = report.get(
        "recommendations",
        {}
    )

    # Recommended roles
    story.append(
        Paragraph(
            "<b>Recommended Roles</b>",
            styles["SubTitle"],
        )
    )

    add_bullet_list(
        story,
        recommendations.get(
            "recommended_roles",
            [],
        ),
        styles,
    )

    # Recommended skills
    story.append(
        Paragraph(
            "<b>Recommended Skills</b>",
            styles["SubTitle"],
        )
    )

    add_bullet_list(
        story,
        recommendations.get(
            "recommended_skills",
            [],
        ),
        styles,
    )

    # Courses
    story.append(
        Paragraph(
            "<b>Recommended Courses</b>",
            styles["SubTitle"],
        )
    )

    courses = recommendations.get(
        "recommended_courses",
        [],
    )

    if courses:
        add_bullet_list(
            story,
            courses,
            styles,
        )
    else:
        story.append(
            Paragraph(
                "No course recommendations available.",
                styles["Body"],
            )
        )

    # Projects
    story.append(
        Paragraph(
            "<b>Recommended Projects</b>",
            styles["SubTitle"],
        )
    )

    projects = recommendations.get(
        "recommended_projects",
        [],
    )

    if projects:
        add_bullet_list(
            story,
            projects,
            styles,
        )
    else:
        story.append(
            Paragraph(
                "No project recommendations available.",
                styles["Body"],
            )
        )

    # Roadmap
    story.append(
        Paragraph(
            "<b>Learning Roadmap</b>",
            styles["SubTitle"],
        )
    )

    roadmap = recommendations.get(
        "learning_roadmap",
        {},
    )

    if roadmap:

        for career, steps in roadmap.items():

            story.append(
                Paragraph(
                    f"<b>{career}</b>",
                    styles["Body"],
                )
            )

            add_bullet_list(
                story,
                steps,
                styles,
            )

    else:

        story.append(
            Paragraph(
                "No learning roadmap available.",
                styles["Body"],
            )
        )

    # Resume tips
    story.append(
        Paragraph(
            "<b>Resume Improvement Tips</b>",
            styles["SubTitle"],
        )
    )

    add_bullet_list(
        story,
        recommendations.get(
            "resume_tips",
            [],
        ),
        styles,
    )

    # ========================================================
    # FOOTER
    # ========================================================

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "Generated by AI Resume Analyzer",
            styles["Small"],
        )
    )

    # ========================================================
    # BUILD PDF
    # ========================================================

    document.build(story)

    return file_path