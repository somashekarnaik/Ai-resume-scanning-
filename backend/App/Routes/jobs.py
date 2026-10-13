from fastapi import (
    APIRouter
)

from ..schemas import (
    JobMatchRequest
)

from ..services.job_matcher import (
    JOBS,
    match_jobs
)


router = APIRouter(
    prefix="/api/jobs",
    tags=["Jobs"]
)


@router.get("/roles")
def list_roles():
    return [
        {
            "title": job["title"],
            "description": job["description"],
            "skills": job["skills"],
        }
        for job in JOBS
    ]


@router.post("/match")
def job_matching(
    data: JobMatchRequest
):

    return match_jobs(
        data.skills
    )