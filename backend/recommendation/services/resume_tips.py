"""
resume_tips.py

Resume Improvement Tips Service
"""


def generate_resume_tips(ats_analysis):
    """
    Generate resume improvement tips based on ATS analysis.

    Parameters
    ----------
    ats_analysis : ATSAnalysis object

    Returns
    -------
    list
        List of resume improvement suggestions.
    """

    tips = []

    # Overall ATS Score
    if ats_analysis.ats_score < 60:
        tips.append(
            "Increase your ATS score by improving keywords, skills, and formatting."
        )

    elif ats_analysis.ats_score < 80:
        tips.append(
            "Your resume is good, but it can be improved with more job-specific keywords."
        )

    else:
        tips.append(
            "Excellent ATS score. Continue tailoring your resume for each job application."
        )

    # Missing Skills
    if ats_analysis.missing_skills:
        tips.append(
            "Add these important skills: "
            + ", ".join(ats_analysis.missing_skills)
        )

    # Weaknesses
    if ats_analysis.weaknesses:
        for weakness in ats_analysis.weaknesses:
            tips.append(weakness)

    # Technical Scores
    if ats_analysis.skill_score < 15:
        tips.append(
            "Expand your technical skills section with relevant programming languages, frameworks, and tools."
        )

    if ats_analysis.project_score < 10:
        tips.append(
            "Include more real-world or academic projects with measurable outcomes."
        )

    if ats_analysis.experience_score < 15:
        tips.append(
            "Add internships, freelance work, or practical experience to strengthen your profile."
        )

    if ats_analysis.education_score < 15:
        tips.append(
            "Provide complete education details, including degree, institution, CGPA, and graduation year."
        )

    if ats_analysis.certification_score < 5:
        tips.append(
            "Add certifications from recognized platforms such as Coursera, AWS, Google, or Microsoft."
        )

    if ats_analysis.format_score < 8:
        tips.append(
            "Improve resume formatting using clear headings, bullet points, and ATS-friendly fonts."
        )

    # Remove duplicate tips
    unique_tips = []

    for tip in tips:
        if tip not in unique_tips:
            unique_tips.append(tip)

    return unique_tips


# ----------------------------------------------------
# Testing
# ----------------------------------------------------

if __name__ == "__main__":

    class DummyATS:

        ats_score = 68
        skill_score = 10
        education_score = 15
        experience_score = 8
        project_score = 6
        certification_score = 2
        format_score = 6

        missing_skills = [
            "SQL",
            "Docker",
            "Git",
        ]

        weaknesses = [
            "GitHub profile is missing",
            "LinkedIn profile is missing",
        ]


    analysis = DummyATS()

    print(generate_resume_tips(analysis))