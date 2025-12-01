from database.connection import get_connection
from utils.response import success, error

class TransactionService:
    @staticmethod
    def transfer(from_user_id, to_username, amount):
        db = get_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM accounts WHERE user_id=%s", (from_user_id,))
        from_acc = cursor.fetchone()

        cursor.execute("SELECT u.id, a.id AS acc_id FROM users u JOIN accounts a ON u.id=a.user_id WHERE username=%s",
                       (to_username,))
        to_user = cursor.fetchone()

        if not to_user:
            return error("Target user not found")

        if from_acc["balance"] < amount:
            return error("Insufficient balance")

        try:
            cursor.execute("UPDATE accounts SET balance=balance-%s WHERE user_id=%s",
                           (amount, from_user_id))
            cursor.execute("UPDATE accounts SET balance=balance+%s WHERE user_id=%s",
                           (amount, to_user["id"]))

            cursor.execute("""
                INSERT INTO transactions(from_acc, to_acc, amount, trx_type)
                VALUES(%s, %s, %s, %s)
            """, (from_acc["id"], to_user["acc_id"], amount, "transfer"))

            db.commit()
            return success("Transfer successful")

        except:
            db.rollback()
            return error("Transaction failed")
