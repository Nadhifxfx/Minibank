from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.customer_service import login_customer

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    pin: str

class LoginResponse(BaseModel):
    token: str

@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest):
    token = login_customer(req.username, req.pin)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": token}
