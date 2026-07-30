def generate_recommendations(data):

    recommendations = []

    if len(data["skills"]) < 5:
        recommendations.append(
            "Add more technical skills."
        )

    if len(data["projects"]) == 0:
        recommendations.append(
            "Include academic or personal projects."
        )

    if len(data["experience"]) == 0:
        recommendations.append(
            "Add internships or work experience."
        )

    if len(data["certifications"]) == 0:
        recommendations.append(
            "Include certifications."
        )

    if not data["linkedin"]:
        recommendations.append(
            "Add your LinkedIn profile."
        )

    if not data["github"]:
        recommendations.append(
            "Add your GitHub profile."
        )

    return recommendations