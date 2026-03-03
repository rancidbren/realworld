from fastapi import APIRouter
from libs.domain.models import HealthStatus

router = APIRouter()

@router.get("/health", response_model=HealthStatus)
def health() -> HealthStatus:
    return HealthStatus()
