from database.connection import get_connection
from utils.security import hash_password, verify_password, create_token
from utils.response import success, error

class AuthService:
    @staticmethod
    def register(username, password):
        db = get_connection()
        cursor = db.cursor()

        cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            return error("Username already exists")

        hashed = hash_password(password)
        cursor.execute("INSERT INTO users(username, password) VALUES(%s, %s)",
                       (username, hashed))
        db.commit()

        user_id = cursor.lastrowid
        cursor.execute("INSERT INTO accounts(user_id, balance) VALUES(%s, 0)", (user_id,))
        db.commit()

        return success("User registered")

    @staticmethod
    def login(username, password):
        db = get_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if not user or not verify_password(password, user["password"]):
            return error("Invalid username or password")

        token = create_token({"user_id": user["id"], "username": user["username"]})

        return success("Login successful", {"token": token})
