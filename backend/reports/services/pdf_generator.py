"""
reports/services/pdf_generator.py

PDF generation service for AI Resume Analyzer.
"""

import os

from django.conf import settings

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)
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
# HELPER FUNCTIONS
# ============================================================

def _safe_text(value, default=""):
    """
    Convert Python values safely into text for ReportLab.
    """

    if value is None:
        return default

    if isinstance(value, (list, tuple)):
        return ", ".join(
            str(item) for item in value
        )

    if isinstance(value, dict):
        return ", ".join(
            f"{key}: {value}"
            for key, value in value.items()
        )

    return str(value)


def _add_bullet_list(story, items, styles):
    """
    Add bullet points to PDF.
    """

    if not items:
        story.append(
            Paragraph(
                "No information available.",
                styles["BodyText"]
            )
        )
        return

    for item in items:

        story.append(
            Paragraph(
                f"• {_safe_text(item)}",
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 4)
        )


def _build_table(data, col_widths=None):
    """
    Create a formatted ReportLab table.
    """

    table = Table(
        data,
        colWidths=col_widths,
        repeatRows=1 if len(data) > 1 else 0,
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey,
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.black,
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
            ]
        )
    )

    return table


# ============================================================
# MAIN PDF GENERATOR
# ============================================================

def generate_pdf(report, output_path):
    """
    Generate PDF from a report dictionary.

    Parameters
    ----------
    report : dict
        Output from build_report()

    output_path : str
        Destination PDF path

    Returns
    -------
    str
        Generated PDF path
    """

    if not report:
        return None

    # Make sure destination directory exists
    output_directory = os.path.dirname(output_path)

    if output_directory:
        os.makedirs(
            output_directory,
            exist_ok=True
        )

    document = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    # Custom title style
    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            spaceAfter=20,
        )
    )

    # Small text style
    styles.add(
        ParagraphStyle(
            name="SmallText",
            parent=styles["BodyText"],
            fontSize=8,
            leading=10,
        )
    )

    story = []

    # ========================================================
    # TITLE
    # ========================================================

    report_info = report.get(
        "report_info",
        {}
    )

    story.append(
        Paragraph(
            _safe_text(
                report_info.get(
                    "title",
                    "AI Resume Analyzer Report"
                )
            ),
            styles["ReportTitle"],
        )
    )

    story.append(
        Paragraph(
            "Generated: "
            + _safe_text(
                report_info.get(
                    "generated_at",
                    ""
                )
            ),
            styles["SmallText"],
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ========================================================
    # CANDIDATE INFORMATION
    # ========================================================

    story.append(
        Paragraph(
            "Candidate Information",
            styles["Heading2"],
        )
    )

    candidate = report.get(
        "candidate",
        {}
    )

    candidate_data = [
        ["Field", "Information"],
        [
            "Resume ID",
            _safe_text(
                candidate.get("resume_id")
            ),
        ],
        [
            "Name",
            _safe_text(
                candidate.get("name"),
                "Not Available"
            ),
        ],
        [
            "Email",
            _safe_text(
                candidate.get("email"),
                "Not Available"
            ),
        ],
        [
            "Phone",
            _safe_text(
                candidate.get("phone"),
                "Not Available"
            ),
        ],
        [
            "Resume File",
            _safe_text(
                candidate.get("resume_file"),
                "Not Available"
            ),
        ],
    ]

    story.append(
        _build_table(
            candidate_data,
            [120, 350]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ========================================================
    # SUMMARY
    # ========================================================

    story.append(
        Paragraph(
            "Resume Analysis Summary",
            styles["Heading2"],
        )
    )

    summary = report.get(
        "summary",
        {}
    )

    summary_data = [
        ["Metric", "Result"],
        [
            "ATS Score",
            f"{summary.get('ats_score', 0)}%",
        ],
        [
            "ATS Category",
            _safe_text(
                summary.get(
                    "ats_category",
                    "Not Analyzed"
                )
            ),
        ],
        [
            "Job Matches",
            _safe_text(
                summary.get(
                    "job_matches",
                    0
                )
            ),
        ],
        [
            "Missing Skills",
            _safe_text(
                summary.get(
                    "missing_skills",
                    0
                )
            ),
        ],
    ]

    story.append(
        _build_table(
            summary_data,
            [200, 270]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ========================================================
    # ATS ANALYSIS
    # ========================================================

    story.append(
        Paragraph(
            "ATS Analysis",
            styles["Heading2"],
        )
    )

    ats = report.get(
        "ats_analysis"
    )

    if ats:

        ats_data = [
            ["Metric", "Score"],
            [
                "ATS Score",
                f"{_safe_text(ats.get('ats_score', 0))}%",
            ],
            [
                "Keyword Score",
                f"{_safe_text(ats.get('keyword_score', 0))}%",
            ],
            [
                "Skill Score",
                f"{_safe_text(ats.get('skill_score', 0))}%",
            ],
            [
                "Education Score",
                f"{_safe_text(ats.get('education_score', 0))}%",
            ],
            [
                "Experience Score",
                f"{_safe_text(ats.get('experience_score', 0))}%",
            ],
            [
                "Project Score",
                f"{_safe_text(ats.get('project_score', 0))}%",
            ],
            [
                "Certification Score",
                f"{_safe_text(ats.get('certification_score', 0))}%",
            ],
            [
                "Format Score",
                f"{_safe_text(ats.get('format_score', 0))}%",
            ],
        ]

        story.append(
            _build_table(
                ats_data,
                [220, 250]
            )
        )

        story.append(
            Spacer(1, 15)
        )

        # Strengths
        story.append(
            Paragraph(
                "Strengths",
                styles["Heading3"],
            )
        )

        _add_bullet_list(
            story,
            ats.get(
                "strengths",
                []
            ),
            styles,
        )

        # Weaknesses
        story.append(
            Spacer(1, 10)
        )

        story.append(
            Paragraph(
                "Weaknesses",
                styles["Heading3"],
            )
        )

        _add_bullet_list(
            story,
            ats.get(
                "weaknesses",
                []
            ),
            styles,
        )

        # Missing skills
        story.append(
            Spacer(1, 10)
        )

        story.append(
            Paragraph(
                "Missing Skills",
                styles["Heading3"],
            )
        )

        _add_bullet_list(
            story,
            ats.get(
                "missing_skills",
                []
            ),
            styles,
        )

        # ATS recommendations
        story.append(
            Spacer(1, 10)
        )

        story.append(
            Paragraph(
                "ATS Recommendations",
                styles["Heading3"],
            )
        )

        _add_bullet_list(
            story,
            ats.get(
                "recommendations",
                []
            ),
            styles,
        )

    else:

        story.append(
            Paragraph(
                "ATS analysis has not been generated.",
                styles["BodyText"],
            )
        )

    # ========================================================
    # JOB MATCHES
    # ========================================================

    story.append(
        Spacer(1, 25)
    )

    story.append(
        Paragraph(
            "Job Match Analysis",
            styles["Heading2"],
        )
    )

    job_matches = report.get(
        "job_matches",
        []
    )

    if job_matches:

        job_data = [
            [
                "Job Title",
                "Score",
                "Level",
            ]
        ]

        for job in job_matches:

            job_data.append(
                [
                    _safe_text(
                        job.get(
                            "job_title",
                            "Unknown Job"
                        )
                    ),
                    f"{_safe_text(job.get('match_score', 0))}%",
                    _safe_text(
                        job.get(
                            "match_level",
                            "Unknown"
                        )
                    ),
                ]
            )

        story.append(
            _build_table(
                job_data,
                [250, 80, 140]
            )
        )

        story.append(
            Spacer(1, 15)
        )

        # Detailed job information
        for index, job in enumerate(
            job_matches,
            start=1
        ):

            story.append(
                Paragraph(
                    f"Job Match {index}: "
                    f"{_safe_text(job.get('job_title'))}",
                    styles["Heading3"],
                )
            )

            description = job.get(
                "description"
            )

            if description:

                story.append(
                    Paragraph(
                        _safe_text(description),
                        styles["BodyText"],
                    )
                )

                story.append(
                    Spacer(1, 8)
                )

            story.append(
                Paragraph(
                    "Matched Skills",
                    styles["Heading4"],
                )
            )

            _add_bullet_list(
                story,
                job.get(
                    "matched_skills",
                    []
                ),
                styles,
            )

            story.append(
                Paragraph(
                    "Missing Skills",
                    styles["Heading4"],
                )
            )

            _add_bullet_list(
                story,
                job.get(
                    "missing_skills",
                    []
                ),
                styles,
            )

    else:

        story.append(
            Paragraph(
                "No job matches are available.",
                styles["BodyText"],
            )
        )

    # ========================================================
    # AI RECOMMENDATIONS
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "AI Career Recommendations",
            styles["Heading2"],
        )
    )

    recommendations = report.get(
        "recommendations",
        {}
    )

    # --------------------------------------------------------
    # Recommended Roles
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Recommended Roles",
            styles["Heading3"],
        )
    )

    _add_bullet_list(
        story,
        recommendations.get(
            "recommended_roles",
            []
        ),
        styles,
    )

    # --------------------------------------------------------
    # Recommended Skills
    # --------------------------------------------------------

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Recommended Skills",
            styles["Heading3"],
        )
    )

    _add_bullet_list(
        story,
        recommendations.get(
            "recommended_skills",
            []
        ),
        styles,
    )

    # --------------------------------------------------------
    # Recommended Courses
    # --------------------------------------------------------

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Recommended Courses",
            styles["Heading3"],
        )
    )

    courses = recommendations.get(
        "recommended_courses",
        []
    )

    if courses:

        for course in courses:

            if isinstance(course, dict):

                title = course.get(
                    "title",
                    "Course"
                )

                description = course.get(
                    "description",
                    ""
                )

                story.append(
                    Paragraph(
                        f"• <b>{_safe_text(title)}</b>",
                        styles["BodyText"],
                    )
                )

                if description:

                    story.append(
                        Paragraph(
                            _safe_text(
                                description
                            ),
                            styles["SmallText"],
                        )
                    )

            else:

                story.append(
                    Paragraph(
                        f"• {_safe_text(course)}",
                        styles["BodyText"],
                    )
                )

            story.append(
                Spacer(1, 5)
            )

    else:

        story.append(
            Paragraph(
                "No course recommendations available.",
                styles["BodyText"],
            )
        )

    # --------------------------------------------------------
    # Recommended Projects
    # --------------------------------------------------------

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Recommended Projects",
            styles["Heading3"],
        )
    )

    projects = recommendations.get(
        "recommended_projects",
        []
    )

    if projects:

        project_data = [
            [
                "Project",
                "Difficulty",
                "Technologies",
            ]
        ]

        for project in projects:

            if isinstance(project, dict):

                project_data.append(
                    [
                        _safe_text(
                            project.get(
                                "title",
                                "Project"
                            )
                        ),
                        _safe_text(
                            project.get(
                                "difficulty",
                                ""
                            )
                        ),
                        _safe_text(
                            project.get(
                                "technologies",
                                []
                            )
                        ),
                    ]
                )

        if len(project_data) > 1:

            story.append(
                _build_table(
                    project_data,
                    [210, 90, 170]
                )
            )

    else:

        story.append(
            Paragraph(
                "No project recommendations available.",
                styles["BodyText"],
            )
        )

    # --------------------------------------------------------
    # Learning Roadmap
    # --------------------------------------------------------

    story.append(
        Spacer(1, 15)
    )

    story.append(
        Paragraph(
            "Learning Roadmap",
            styles["Heading3"],
        )
    )

    roadmap = recommendations.get(
        "learning_roadmap",
        {}
    )

    if roadmap:

        for career, steps in roadmap.items():

            story.append(
                Paragraph(
                    _safe_text(career),
                    styles["Heading4"],
                )
            )

            _add_bullet_list(
                story,
                steps,
                styles,
            )

            story.append(
                Spacer(1, 8)
            )

    else:

        story.append(
            Paragraph(
                "No learning roadmap available.",
                styles["BodyText"],
            )
        )

    # --------------------------------------------------------
    # Resume Tips
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Resume Improvement Tips",
            styles["Heading3"],
        )
    )

    _add_bullet_list(
        story,
        recommendations.get(
            "resume_tips",
            []
        ),
        styles,
    )

    # ========================================================
    # BUILD PDF
    # ========================================================

    document.build(story)

    return output_path


# ============================================================
# IMPORTANT WRAPPER USED BY views.py
# ============================================================

def generate_pdf_report(
    resume_id,
    output_path=None
):
    """
    Generate PDF directly from Resume ID.

    This function is required by reports/views.py.
    """

    report = build_report(
        resume_id
    )

    if not report:
        return None

    if output_path is None:

        reports_directory = os.path.join(
            settings.MEDIA_ROOT,
            "reports",
        )

        os.makedirs(
            reports_directory,
            exist_ok=True
        )

        output_path = os.path.join(
            reports_directory,
            f"report_{resume_id}.pdf"
        )

    return generate_pdf(
        report,
        output_path
    )