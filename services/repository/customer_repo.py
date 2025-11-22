from db.connection import SessionLocal
from db.models import Customer

class CustomerRepository:

    def get_customer_by_username(self, username):
        session = SessionLocal()
        try:
            return session.query(Customer).filter(
                Customer.customer_username == username
            ).first()
        finally:
            session.close()
