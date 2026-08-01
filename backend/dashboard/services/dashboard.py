"""
dashboard.py

Main dashboard service.
Combines statistics and chart data.
"""

from parser.models import Resume
from analyzer.models import ATSAnalysis

from .statistics import get_dashboard_statistics
from .charts import get_dashboard_charts


def get_dashboard_data(user):
    """
    Generate complete dashboard data for the user.
    """

    # ==========================================
    # Statistics
    # ==========================================

    statistics = get_dashboard_statistics(user)

    # ==========================================
    # Charts
    # ==========================================

    charts = get_dashboard_charts(user)

    # ==========================================
    # Recent Resume
    # ==========================================

    latest_resume = (
        Resume.objects
        .filter(user=user)
        .order_by("-uploaded_at")
        .first()
    )

    recent_resume = None

    if latest_resume:

        ats_analysis = (
            ATSAnalysis.objects
            .filter(resume=latest_resume)
            .first()
        )

        recent_resume = {
            "id": latest_resume.id,
            "full_name": latest_resume.full_name,
            "email": latest_resume.email,
            "uploaded_at": latest_resume.uploaded_at,
            "ats_score": (
                ats_analysis.ats_score
                if ats_analysis
                else 0
            ),
        }

    # ==========================================
    # Final Dashboard Response
    # ==========================================

    return {
        "statistics": statistics,
        "charts": charts,
        "recent_resume": recent_resume,
    }