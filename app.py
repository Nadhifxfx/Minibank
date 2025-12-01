from fastapi import FastAPI
from route.auth_route import router as auth_router
from route.account_route import router as account_router
from route.transaction_route import router as transaction_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(account_router, prefix="/account")
app.include_router(transaction_router, prefix="/transaction")
