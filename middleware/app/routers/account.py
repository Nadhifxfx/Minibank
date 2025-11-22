from fastapi import APIRouter, Depends, HTTPException
from app.deps import get_current_user
from app.services.service_client import get_from_service

router = APIRouter(prefix="/account", tags=["account"])

@router.get("/balance/{customer_id}")
async def get_balance(customer_id: int, user=Depends(get_current_user)):
    # ensure the jwt customer_id matches requested customer or user has admin role
    if user["customer_id"] != customer_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        res = await get_from_service(f"/account/balance/{customer_id}")
    except Exception:
        raise HTTPException(status_code=502, detail="Service error")
    # normalize response
    return res
