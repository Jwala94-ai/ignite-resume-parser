from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.pdf_generator import (
    PDFGenerator
)

router = APIRouter()


@router.post("/report")
async def generate_report(
    result: dict
):

    file_name = "report.pdf"

    PDFGenerator.generate(
        result,
        file_name
    )

    return FileResponse(
        file_name,
        media_type="application/pdf",
        filename="Ignite_Report.pdf"
    )