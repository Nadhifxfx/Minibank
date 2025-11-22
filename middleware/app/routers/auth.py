from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.auth import LoginRequest
from app.security.jwt_handler import create_access_token, create_refresh_token
from app.services.service_client import post_to_service
from app.security.token_blacklist import add_blacklist
from app.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(payload: LoginRequest):
    # forward to service for credential check (service handles PIN hashing check)
    try:
        res = await post_to_service("/auth/validate", payload.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail="Service unavailable")

    if res.get("status") != "OK":
        raise HTTPException(status_code=401, detail=res.get("message", "invalid credentials"))

    user = res["data"]
    access = create_access_token({"customer_id": user["id"], "username": user["customer_username"]})
    refresh = create_refresh_token({"customer_id": user["id"], "username": user["customer_username"]})
    return {"status": "OK", "data": {"access_token": access, "refresh_token": refresh, "customer_id": user["id"]}}

@router.post("/refresh")
async def refresh(token: dict):
    # accept refresh token, decode, issue new access
    from app.security.jwt_handler import decode_token
    try:
        payload = decode_token(token["refresh_token"])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid token type")
    new_access = create_access_token({"customer_id": payload["customer_id"], "username": payload["username"]})
    return {"status": "OK", "data": {"access_token": new_access}}

@router.post("/logout")
async def logout(credentials=Depends(get_current_user)):
    access_token = credentials.get("raw_token") if credentials.get("raw_token") else None
    # best if get token from Authorization header and blacklist it
    from fastapi import Request
    # here just expect client to pass token; alternatively implement server-side session
    # For demo, assume body contains token string
    return {"status": "OK", "message": "Logged out"}
