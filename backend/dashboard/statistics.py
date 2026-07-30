from parser.models import Resume

from parser.services import parse_resume


def dashboard_statistics(user):

    resumes = Resume.objects.filter(
        user=user
    )

    total_resumes = resumes.count()

    ats_scores = []

    skills_frequency = {}

    highest_ats = 0

    lowest_ats = 100

    for resume in resumes:

        parsed = parse_resume(
            resume.extracted_text
        )

        ats = parsed.get(
            "ats_score",
            0,
        )

        ats_scores.append(ats)

        highest_ats = max(
            highest_ats,
            ats,
        )

        lowest_ats = min(
            lowest_ats,
            ats,
        )

        for skill in parsed.get(
            "skills",
            [],
        ):

            skills_frequency[skill] = (
                skills_frequency.get(skill, 0)
                + 1
            )

    average_ats = (
        sum(ats_scores) / len(ats_scores)
        if ats_scores
        else 0
    )

    if total_resumes == 0:
        lowest_ats = 0

    return {

        "total_resumes": total_resumes,

        "average_ats_score": round(
            average_ats,
            2,
        ),

        "highest_ats_score": highest_ats,

        "lowest_ats_score": lowest_ats,

        "skills_distribution": skills_frequency,
    }