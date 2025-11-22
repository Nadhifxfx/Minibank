from fastapi import APIRouter, Depends, HTTPException
from app.deps import get_current_user
from app.schemas.transaction import TransferRequest
from app.services.service_client import post_to_service

router = APIRouter(prefix="/transaction", tags=["transaction"])

@router.post("/transfer")
async def transfer(req: TransferRequest, user=Depends(get_current_user)):
    # basic checks: customer identity
    if user["customer_id"] != req.customer_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    # forward to services
    try:
        resp = await post_to_service("/transaction/transfer", {
            "customer_id": req.customer_id,
            "from": req.from_acc,
            "to": req.to_acc,
            "amount": float(req.amount)
        })
    except Exception:
        raise HTTPException(status_code=502, detail="Service error")
    return resp
