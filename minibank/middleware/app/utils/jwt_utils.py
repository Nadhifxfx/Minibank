from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "MINIBANKSECRETTOKEN"
ALGORITHM = "HS256"

def create_token(data: dict):
    data["exp"] = datetime.utcnow() + timedelta(minutes=30)
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
