from fastapi import APIRouter, Header
from utils.security import decode_token
from services.transaction_service import TransactionService

router = APIRouter()

@router.post("/transfer")
def transfer(data: dict, token: str = Header(None)):
    user = decode_token(token)
    return TransactionService.transfer(
        user_id=user["user_id"],
        to_username=data["to_username"],
        amount=data["amount"]
    )
