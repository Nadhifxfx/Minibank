from models import Customer
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

def validate_login(db: Session, username: str, pin: str):
    user = db.query(Customer).filter(Customer.customer_username == username).first()
    if not user:
        return None, "USER_NOT_FOUND"

    if not bcrypt.verify(pin, user.customer_pin):
        user.failed_login_attempts += 1
        db.commit()
        return None, "INVALID_PIN"
    
    user.failed_login_attempts = 0
    db.commit()
    return user, "SUCCESS"
