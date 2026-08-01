"""
Languages Parser
"""


LANGUAGES = [
    "English",
    "Hindi",
    "Telugu",
    "Tamil",
    "Kannada",
    "Malayalam",
    "French",
    "German",
    "Spanish",
]


def extract_languages(text):
    """
    Extract spoken languages.
    """

    found = []

    if not text:
        return found

    text = text.lower()

    for language in LANGUAGES:

        if language.lower() in text:
            found.append(language)

    return list(dict.fromkeys(found))