from parser.models import Resume


def delete_resume(user, resume_id):
    """
    Delete a resume belonging to the user.
    """

    try:
        resume = Resume.objects.get(
            id=resume_id,
            user=user,
        )
    except Resume.DoesNotExist:
        return False

    resume.delete()

    return True