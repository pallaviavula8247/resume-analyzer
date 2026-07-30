def generate_job_recommendations(result):

    recommendations = []

    if result["match_score"] >= 90:

        recommendations.append(
            "Excellent match for this job."
        )

    elif result["match_score"] >= 75:

        recommendations.append(
            "Good match. Improve a few missing skills."
        )

    elif result["match_score"] >= 50:

        recommendations.append(
            "Moderate match. Add the missing technical skills."
        )

    else:

        recommendations.append(
            "Low match. Resume requires significant improvement."
        )

    if result["missing_skills"]:

        recommendations.append(
            "Learn: "
            + ", ".join(result["missing_skills"])
        )

    return recommendations