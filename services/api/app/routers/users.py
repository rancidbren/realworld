from fastapi import APIRouter, Depends, HTTPException
from libs.domain.models import UserCreate, UserPublic
from services.api.app.state import user_repo
from services.api.app.deps import get_current_user_id

router = APIRouter()

@router.post("", response_model=UserPublic, status_code=201)
def create_user(data: UserCreate) -> UserPublic:
    user = user_repo.create(data)
    return UserPublic(**user.model_dump())

@router.get("/me", response_model=UserPublic)
def me(user_id: str = Depends(get_current_user_id)) -> UserPublic:
    user = user_repo.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserPublic(**user.model_dump())
