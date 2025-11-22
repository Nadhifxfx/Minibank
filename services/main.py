from fastapi import FastAPI
from handler.account_handler import AccountHandler
from handler.transaction_handler import TransactionHandler

app = FastAPI()

@app.get("/account/balance/{customer_id}")
def balance(customer_id: int):
    handler = AccountHandler()
    return handler.get_balance(customer_id)


@app.post("/transaction/transfer")
def transfer(data: dict):
    handler = TransactionHandler()
    return handler.transfer(
        customer_id=data["customer_id"],
        from_acc=data["from"],
        to_acc=data["to"],
        amount=data["amount"]
    )
