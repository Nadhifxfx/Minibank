from models import Portfolio
from sqlalchemy.orm import Session

def get_balance(db: Session, customer_id: int):
    accounts = db.query(Portfolio).filter(
        Portfolio.m_customer_id == customer_id
    ).all()
    return accounts
