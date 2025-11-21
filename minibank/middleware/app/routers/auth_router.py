from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import LoginRequest, LoginResponse
from app.services.customer_service import login_customer

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    token = login_customer(request.username, request.pin)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid Username or PIN")
    return {"token": token}
