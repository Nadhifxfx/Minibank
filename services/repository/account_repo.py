from db.connection import SessionLocal
from db.models import PortfolioAccount

class AccountRepository:

    def get_account_by_customer(self, cust_id):
        session = SessionLocal()
        try:
            return session.query(PortfolioAccount).filter(
                PortfolioAccount.m_customer_id == cust_id
            ).first()
        finally:
            session.close()

    def update_balance(self, account_number, new_balance):
        session = SessionLocal()
        try:
            acc = session.query(PortfolioAccount).filter(
                PortfolioAccount.account_number == account_number
            ).first()

            if acc:
                acc.available_balance = new_balance
                session.commit()

            return acc
        except:
            session.rollback()
            raise
        finally:
            session.close()
