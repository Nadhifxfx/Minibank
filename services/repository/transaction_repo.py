from db.connection import SessionLocal
from db.models import Transaction
from datetime import datetime

class TransactionRepository:

    def insert_transaction(self, data):
        session = SessionLocal()
        try:
            trx = Transaction(
                m_customer_id=data["customer_id"],
                transaction_amount=data["amount"],
                from_account_number=data["from"],
                to_account_number=data["to"],
                status=data["status"],
                description=data["description"],
                transaction_date=datetime.now(),
            )
            session.add(trx)
            session.commit()
            return trx
        except:
            session.rollback()
            raise
        finally:
            session.close()
