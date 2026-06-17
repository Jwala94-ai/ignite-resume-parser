from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


class PDFGenerator:

    @staticmethod
    def generate(result, filename):

        pdf = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "Ignite Resume Analysis Report",
                styles["Title"]
            )
        )

        content.append(Spacer(1, 20))

        ats = result.get("ats", {})

        content.append(
            Paragraph(
                f"ATS Score: {ats.get('ats_score', 0)}%",
                styles["Heading2"]
            )
        )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Strengths",
                styles["Heading2"]
            )
        )

        for item in ats.get(
            "strengths",
            []
        ):
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Weaknesses",
                styles["Heading2"]
            )
        )

        for item in ats.get(
            "weaknesses",
            []
        ):
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Technical Skills",
                styles["Heading2"]
            )
        )

        for skill in result["skills"][
            "technical"
        ]:
            content.append(
                Paragraph(
                    f"• {skill}",
                    styles["BodyText"]
                )
            )

        pdf.build(content)