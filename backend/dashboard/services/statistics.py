"""
statistics.py

Calculates dashboard statistics.
"""

from parser.models import Resume
from analyzer.models import ATSAnalysis, JobMatch
from recommendation.models import Recommendation


def get_dashboard_statistics(user):
    """
    Calculate dashboard statistics for the logged-in user.
    """

    resumes = Resume.objects.filter(user=user)

    analyses = ATSAnalysis.objects.filter(
        resume__user=user
    )

    job_matches = JobMatch.objects.filter(
        resume__user=user
    )

    recommendations = Recommendation.objects.filter(
        resume__user=user
    )

    total_resumes = resumes.count()

    total_job_matches = job_matches.count()

    total_recommendations = recommendations.count()

    if analyses.exists():

        ats_scores = [
            analysis.ats_score
            for analysis in analyses
        ]

        average_ats_score = round(
            sum(ats_scores) / len(ats_scores),
            2,
        )

        highest_ats_score = max(ats_scores)

    else:

        average_ats_score = 0

        highest_ats_score = 0

    return {
        "total_resumes": total_resumes,
        "average_ats_score": average_ats_score,
        "highest_ats_score": highest_ats_score,
        "total_job_matches": total_job_matches,
        "total_recommendations": total_recommendations,
    }