from datetime import datetime, timedelta, timezone
from jose import jwt
from typing import Any, Dict
from libs.config.settings import settings

def create_access_token(sub: str, extra_claims: Dict[str, Any] | None = None) -> str:
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=settings.jwt_exp_minutes)
    payload: Dict[str, Any] = {"sub": sub, "iat": int(now.timestamp()), "exp": int(exp.timestamp())}
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
