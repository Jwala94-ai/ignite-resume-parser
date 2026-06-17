from fastapi import APIRouter, UploadFile, File
import os

from app.services.parser_service import ParserService

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(
            await file.read()
        )

    try:

        result = ParserService().parse(
            file_path
        )

        return result

    except Exception as e:

        return {
            "error": str(e)
        }