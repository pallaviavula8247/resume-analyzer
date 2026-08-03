"""
reports/services/pdf_generator.py

Generate PDF report for AI Resume Analyzer.
"""


from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet



def generate_pdf(report, output_path):

    """
    Generate resume analysis PDF.

    Args:
        report: dictionary from build_report()
        output_path: pdf file path
    """


    document = SimpleDocTemplate(
        output_path,
        pagesize=A4
    )


    styles = getSampleStyleSheet()


    story = []



    # --------------------------------
    # Title
    # --------------------------------

    story.append(
        Paragraph(
            report["report_info"]["title"],
            styles["Title"]
        )
    )


    story.append(
        Spacer(1,20)
    )



    # --------------------------------
    # Candidate Details
    # --------------------------------

    story.append(
        Paragraph(
            "Candidate Information",
            styles["Heading2"]
        )
    )


    candidate = report["candidate"]


    candidate_data = [

        ["Name", candidate["name"]],

        ["Email", candidate["email"]],

        ["Phone", candidate["phone"]],

    ]


    table = Table(
        candidate_data
    )


    table.setStyle(
        TableStyle(
            [
                ("GRID",(0,0),(-1,-1),0.5,None)
            ]
        )
    )


    story.append(table)

    story.append(
        Spacer(1,20)
    )



    # --------------------------------
    # ATS Summary
    # --------------------------------


    story.append(
        Paragraph(
            "ATS Analysis Summary",
            styles["Heading2"]
        )
    )


    summary = report["summary"]


    ats_data = [

        ["ATS Score",
         str(summary["ats_score"])+"%"],


        ["Category",
         summary["ats_category"]],


        ["Job Matches",
         str(summary["job_matches"])]

    ]



    ats_table = Table(
        ats_data
    )


    ats_table.setStyle(
        TableStyle(
            [
                ("GRID",(0,0),(-1,-1),0.5,None)
            ]
        )
    )


    story.append(
        ats_table
    )


    story.append(
        Spacer(1,20)
    )



    # --------------------------------
    # ATS Details
    # --------------------------------


    ats = report["ats_analysis"]


    if ats:


        story.append(
            Paragraph(
                "Strengths",
                styles["Heading3"]
            )
        )


        for item in ats["strengths"]:

            story.append(
                Paragraph(
                    "• "+item,
                    styles["BodyText"]
                )
            )


        story.append(
            Spacer(1,10)
        )



        story.append(
            Paragraph(
                "Weaknesses",
                styles["Heading3"]
            )
        )


        for item in ats["weaknesses"]:

            story.append(
                Paragraph(
                    "• "+item,
                    styles["BodyText"]
                )
            )



        story.append(
            Spacer(1,10)
        )



        story.append(
            Paragraph(
                "Missing Skills",
                styles["Heading3"]
            )
        )


        for skill in ats["missing_skills"]:

            story.append(
                Paragraph(
                    "• "+skill,
                    styles["BodyText"]
                )
            )



    # --------------------------------
    # Job Matches
    # --------------------------------


    story.append(
        Spacer(1,20)
    )


    story.append(
        Paragraph(
            "Job Match Analysis",
            styles["Heading2"]
        )
    )


    job_data = [

        [
            "Job",
            "Score",
            "Level"
        ]

    ]


    for job in report["job_matches"]:


        job_data.append(

            [

                job["job_title"],

                str(job["match_score"])+"%",

                job["match_level"]

            ]

        )



    job_table = Table(
        job_data
    )


    job_table.setStyle(
        TableStyle(
            [
                ("GRID",(0,0),(-1,-1),0.5,None)
            ]
        )
    )


    story.append(
        job_table
    )



    # --------------------------------
    # Recommendations
    # --------------------------------


    story.append(
        Spacer(1,20)
    )


    story.append(
        Paragraph(
            "AI Recommendations",
            styles["Heading2"]
        )
    )


    for rec in ats["recommendations"]:

        story.append(

            Paragraph(
                "• "+rec,
                styles["BodyText"]
            )

        )



    document.build(
        story
    )


    return output_path