from database.connection import get_connection
from utils.response import success, error

class AccountService:
    @staticmethod
    def get_balance(user_id):
        db = get_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM accounts WHERE user_id=%s", (user_id,))
        acc = cursor.fetchone()

        if not acc:
            return error("Account not found")

        return success("Balance fetched", {"balance": float(acc["balance"])})
