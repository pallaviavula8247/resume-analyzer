import pdfplumber
import docx


def extract_text(file_path):
    """
    Extract text from PDF or DOCX.
    """

    text = ""

    if file_path.lower().endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    elif file_path.lower().endswith(".docx"):

        document = docx.Document(file_path)

        for para in document.paragraphs:
            text += para.text + "\n"

    return text