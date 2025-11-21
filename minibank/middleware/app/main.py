from fastapi import FastAPI
from app.routers import auth_router, customer_router, transaction_router

app = FastAPI(title="Mini Bank API")

app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(customer_router.router, prefix="/customers", tags=["Customer"])
app.include_router(transaction_router.router, prefix="/transactions", tags=["Transaction"])
