from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, condecimal
from app.dependencies import get_current_user
from app.services.transaction_service import (
    get_transactions_by_customer,
    transfer_internal,
    transfer_interbank
)

router = APIRouter()

class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    to_bank_code: str | None = None
    amount: condecimal(max_digits=30, decimal_places=5)
    description: str | None = None

@router.post("/transfer")
def transfer(req: TransferRequest, user_id: int = Depends(get_current_user)):
    # Determine internal vs interbank by presence of to_bank_code
    if req.to_bank_code:
        # Interbank
        result = transfer_interbank(user_id, req.from_account, req.to_account, req.to_bank_code, float(req.amount), req.description)
    else:
        # Internal transfer
        result = transfer_internal(user_id, req.from_account, req.to_account, float(req.amount), req.description)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return {"success": True, "transaction_id": result.get("transaction_id")}

@router.get("/history")
def history(user_id: int = Depends(get_current_user)):
    return get_transactions_by_customer(user_id)
