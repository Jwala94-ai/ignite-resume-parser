"""Resume parser service"""

from app.parsers.document_loader import DocumentLoader
from app.parsers.section_detector import SectionDetector
from app.ai.extractor import AIExtractor
from app.scorer.ats_scorer import ATSScorer


class ParserService:

    def parse(self, file_path):

        # Load document
        if file_path.lower().endswith(".pdf"):

            text = DocumentLoader.load_pdf(
                file_path
            )

        elif file_path.lower().endswith(".docx"):

            text = DocumentLoader.load_docx(
                file_path
            )

        else:

            raise ValueError(
                "Unsupported file format"
            )

        # Detect sections
        sections = SectionDetector().detect(
            text
        )

        # Extract structured information
        result = AIExtractor().extract(
            text,
            sections
        )

        # ATS scoring
        ats_result = ATSScorer().score(
            result
        )

        result["ats"] = ats_result

        return result