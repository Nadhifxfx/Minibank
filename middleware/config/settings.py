import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "minibank")
DB_PASS = os.getenv("DB_PASS", "minibank123")
DB_NAME = os.getenv("DB_NAME", "ebanking")

JWT_SECRET = os.getenv("JWT_SECRET", "MINIBANKSECRET-CHANGE")
JWT_ALGORITHM = "HS256"
JWT_EXP_MINUTES = int(os.getenv("JWT_EXP_MINUTES", 60))
