from sqlalchemy import Column, Integer, String, BigInteger, Numeric, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "m_customer"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    customer_name = Column(String(30), nullable=False)
    customer_username = Column(String(50), nullable=False)
    customer_pin = Column(String(200), nullable=False)
    customer_phone = Column(String(20))
    customer_email = Column(String(50))
    cif_number = Column(String(30))
    failed_login_attempts = Column(Integer, default=0)
    mb_status = Column(String(1))
    created = Column(TIMESTAMP)
    updated = Column(TIMESTAMP)


class PortfolioAccount(Base):
    __tablename__ = "m_portfolio_account"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    m_customer_id = Column(BigInteger)
    account_number = Column(String(20))
    account_status = Column(String(1))
    account_name = Column(String(50))
    account_type = Column(String(10))
    currency_code = Column(String(3))
    clear_balance = Column(Numeric(30, 5))
    available_balance = Column(Numeric(30, 5))
    created = Column(TIMESTAMP)
    updated = Column(TIMESTAMP)


class Transaction(Base):
    __tablename__ = "t_transaction"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    m_customer_id = Column(BigInteger)
    transaction_amount = Column(Numeric(30,5))
    from_account_number = Column(String(20))
    to_account_number = Column(String(20))
    reference_number = Column(String(12))
    status = Column(String(10))
    description = Column(String(250))
    transaction_date = Column(TIMESTAMP)
