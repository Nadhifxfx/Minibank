from fastapi import APIRouter
from services.auth_service import AuthService

router = APIRouter()

@router.post("/register")
def register(data: dict):
    return AuthService.register(data["username"], data["password"])

@router.post("/login")
def login(data: dict):
    return AuthService.login(data["username"], data["password"])
