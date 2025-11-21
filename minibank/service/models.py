from sqlalchemy import Column, BigInteger, String, Numeric, DateTime, Integer
from sqlalchemy.sql import func
from database import Base

class Customer(Base):
    __tablename__ = 'm_customer'

    id = Column(BigInteger, primary_key=True, index=True)
    customer_name = Column(String(30), nullable=False)
    customer_username = Column(String(50), nullable=False, unique=True)
    customer_pin = Column(String(200), nullable=False)
    customer_phone = Column(String(20))
    failed_login_attempts = Column(Integer, default=0)
    mb_status = Column(String(1))
    created = Column(DateTime, server_default=func.now())

class Portfolio(Base):
    __tablename__ = 'm_portfolio_account'

    id = Column(BigInteger, primary_key=True, index=True)
    m_customer_id = Column(BigInteger)
    account_number = Column(String(20))
    account_status = Column(String(1))
    available_balance = Column(Numeric(30, 5))
    created = Column(DateTime, server_default=func.now())

class Transaction(Base):
    __tablename__ = 't_transaction'

    id = Column(BigInteger, primary_key=True, index=True)
    m_customer_id = Column(BigInteger)
    transaction_amount = Column(Numeric(30,5))
    from_account_number = Column(String(20))
    to_account_number = Column(String(20))
    status = Column(String(10))
    created = Column(DateTime, server_default=func.now())
