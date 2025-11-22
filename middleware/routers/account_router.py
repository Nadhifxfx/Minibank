from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from app.services.customer_service import get_customer_profile, get_accounts_by_customer

router = APIRouter()

@router.get("/me")
def me(user_id: int = Depends(get_current_user)):
    customer = get_customer_profile(user_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/accounts")
def accounts(user_id: int = Depends(get_current_user)):
    return get_accounts_by_customer(user_id)
