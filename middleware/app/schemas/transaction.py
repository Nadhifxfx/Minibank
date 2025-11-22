from pydantic import BaseModel, condecimal
class TransferRequest(BaseModel):
    customer_id: int
    from_acc: str
    to_acc: str
    amount: condecimal(gt=0)
