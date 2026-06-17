from fastapi import APIRouter
from pydantic import BaseModel

from app.matcher.jd_matcher import JDMatcher

router = APIRouter()


class MatchRequest(BaseModel):
    resume: dict
    job_description: str


@router.post("/match")
def match_resume(
    request: MatchRequest
):

    result = JDMatcher().match(
        request.resume,
        request.job_description
    )

    return result