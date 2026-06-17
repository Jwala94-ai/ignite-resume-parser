import fitz
from docx import Document


class DocumentLoader:

    @staticmethod
    def load_pdf(path):

        doc = fitz.open(path)

        text = ""

        for page in doc:
            text += page.get_text()

        return text

    @staticmethod
    def load_docx(path):

        doc = Document(path)

        return "\n".join(
            para.text
            for para in doc.paragraphs
        )