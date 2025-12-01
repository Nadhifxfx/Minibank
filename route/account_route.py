from fastapi import APIRouter, Header
from utils.security import decode_token
from services.account_service import AccountService

router = APIRouter()

@router.get("/balance")
def balance(token: str = Header(None)):
    user = decode_token(token)
    return AccountService.get_balance(user["user_id"])
