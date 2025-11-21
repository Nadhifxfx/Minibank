from sqlalchemy.orm import Session
from models import Portfolio, Transaction
from decimal import Decimal

def transfer(db: Session, customer_id: int, from_acc: str, to_acc: str, amount: float):

    sender = db.query(Portfolio).filter(
        Portfolio.account_number == from_acc,
        Portfolio.m_customer_id == customer_id
    ).first()

    receiver = db.query(Portfolio).filter(
        Portfolio.account_number == to_acc
    ).first()

    if not sender or sender.available_balance < Decimal(amount):
        return "INSUFFICIENT_FUNDS"

    sender.available_balance -= Decimal(amount)
    receiver.available_balance += Decimal(amount)

    trx = Transaction(
        m_customer_id=customer_id,
        transaction_amount=amount,
        from_account_number=from_acc,
        to_account_number=to_acc,
        status="SUCCESS"
    )
    db.add(trx)
    db.commit()

    return "TRANSFER_SUCCESS"
