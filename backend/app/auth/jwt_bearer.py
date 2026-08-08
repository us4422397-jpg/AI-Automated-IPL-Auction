import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from typing import Optional
import uuid
from app.config import get_settings

settings = get_settings()
security = HTTPBearer()

class CurrentUser(BaseModel):
    user_id: uuid.UUID
    franchise_id: Optional[uuid.UUID]
    role: Optional[str]
    email: Optional[str]

def verify_jwt(credentials: HTTPAuthorizationCredentials = Security(security)) -> CurrentUser:
    token = credentials.credentials
    try:
        # Supabase signs JWTs with the SUPABASE_JWT_SECRET
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        
        user_metadata = payload.get("user_metadata", {})
        
        return CurrentUser(
            user_id=uuid.UUID(payload.get("sub")),
            franchise_id=uuid.UUID(user_metadata.get("franchise_id")) if user_metadata.get("franchise_id") else None,
            role=user_metadata.get("role", "viewer"),
            email=payload.get("email")
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(user: CurrentUser = Security(verify_jwt)) -> CurrentUser:
    return user
