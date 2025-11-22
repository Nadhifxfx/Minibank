from passlib.hash import bcrypt

def hash_pin(pin: str):
    return bcrypt.hash(pin)

def verify_pin(pin: str, hashed: str):
    return bcrypt.verify(pin, hashed)
