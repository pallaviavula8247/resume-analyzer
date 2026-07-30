def calculate_ats_score(data):

    score = 0

    if data["full_name"]:
        score += 10

    if data["email"]:
        score += 10

    if data["phone"]:
        score += 10

    if len(data["skills"]) >= 5:
        score += 20

    if len(data["education"]) > 0:
        score += 15

    if len(data["experience"]) > 0:
        score += 15

    if len(data["projects"]) > 0:
        score += 10

    if len(data["certifications"]) > 0:
        score += 10

    return min(score, 100)