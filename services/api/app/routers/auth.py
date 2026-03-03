from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from libs.security.jwt import create_access_token
from services.api.app.state import user_repo

router = APIRouter()

class TokenRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/token", response_model=TokenResponse)
def token(req: TokenRequest) -> TokenResponse:
    user = user_repo.verify_login(req.email, req.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return TokenResponse(access_token=create_access_token(sub=user.id))
