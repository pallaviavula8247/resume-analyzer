"""
reports/services/report_builder.py

Build complete report data for PDF generation.
"""

from datetime import datetime

from django.utils import timezone

from parser.models import Resume
from analyzer.models import ATSAnalysis, JobMatch
from recommendation.models import Recommendation



def get_score_category(score):
    """
    Convert ATS score into readable category.
    """

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Needs Improvement"



def format_date(value):
    """
    Format datetime for PDF display.
    """

    if not value:
        return ""

    return value.strftime(
        "%d %B %Y, %I:%M %p"
    )



def build_report(resume_id):
    """
    Build complete AI Resume Analyzer report.

    Used for:
    - PDF generation
    - Dashboard reports
    - API response

    Returns:
        dict
    """

    try:
        resume = Resume.objects.get(
            id=resume_id
        )

    except Resume.DoesNotExist:
        return None



    # -----------------------------
    # Fetch ATS Analysis
    # -----------------------------

    try:
        ats = ATSAnalysis.objects.get(
            resume=resume
        )

    except ATSAnalysis.DoesNotExist:
        ats = None



    # -----------------------------
    # Fetch Job Matches
    # -----------------------------

    job_matches = JobMatch.objects.filter(
        resume=resume
    )



    # -----------------------------
    # Fetch AI Recommendations
    # -----------------------------

    recommendations = Recommendation.objects.filter(
        resume=resume
    )



    report = {


        # =============================
        # REPORT INFORMATION
        # =============================

        "report_info": {

            "title":
            "AI Resume Analyzer Report",

            "generated_at":
            format_date(
                timezone.now()
            ),

            "version":
            "1.0"

        },



        # =============================
        # CANDIDATE INFORMATION
        # =============================

        "candidate": {

            "resume_id":
            resume.id,

            "name":
            getattr(
                resume,
                "full_name",
                ""
            ),

            "email":
            getattr(
                resume,
                "email",
                ""
            ),

            "phone":
            getattr(
                resume,
                "phone",
                ""
            ),

            "resume_file":
            getattr(
                resume,
                "file",
                ""
            ),

        },



        # =============================
        # SUMMARY
        # =============================

        "summary": {

            "ats_score":
            ats.ats_score if ats else 0,


            "ats_category":
            get_score_category(
                ats.ats_score
            )
            if ats else "Not Analyzed",


            "job_matches":
            job_matches.count(),


            "missing_skills":
            len(
                ats.missing_skills
            )
            if ats else 0

        },



        # =============================
        # ATS ANALYSIS
        # =============================

        "ats_analysis": None,



        # =============================
        # JOB MATCHES
        # =============================

        "job_matches": [],



        # =============================
        # RECOMMENDATIONS
        # =============================

        "recommendations": []

    }



    # =====================================
    # ATS DATA
    # =====================================

    if ats:

        report["ats_analysis"] = {


            "ats_score":
            ats.ats_score,


            "keyword_score":
            ats.keyword_score,


            "skill_score":
            ats.skill_score,


            "education_score":
            ats.education_score,


            "experience_score":
            ats.experience_score,


            "project_score":
            ats.project_score,


            "certification_score":
            ats.certification_score,


            "format_score":
            ats.format_score,



            "strengths":
            ats.strengths,


            "weaknesses":
            ats.weaknesses,


            "missing_skills":
            ats.missing_skills,


            "recommendations":
            ats.recommendations,


            "analyzed_at":
            format_date(
                ats.analyzed_at
            )

        }



    # =====================================
    # JOB MATCH DATA
    # =====================================

    for job in job_matches:


        report["job_matches"].append({


            "job_title":
            job.job_title,


            "description":
            job.job_description,


            "match_score":
            job.match_score,


            "match_level":
            job.match_level,


            "matched_skills":
            job.matched_skills,


            "missing_skills":
            job.missing_skills,


            "extra_skills":
            job.extra_skills,


            "recommendations":
            job.recommendations,


            "created_at":
            format_date(
                job.created_at
            )

        })



    # =====================================
    # AI RECOMMENDATIONS
    # =====================================

    for item in recommendations:


        report["recommendations"].append({


            "title":
            getattr(
                item,
                "title",
                ""
            ),


            "description":
            getattr(
                item,
                "description",
                ""
            )

        })



    return report